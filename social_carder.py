import argparse
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.parse
from pathlib import Path
import shutil

import niquests
from PIL import Image

"""
See "[From Bashful to Social Butterfly: Automating Link Previews for Zola Sites](https://osc.garden/blog/automating-social-media-cards-zola/)"
"""


def parse_arguments():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="""
This script automates the creation of social media cards for Zola websites.
It takes a Markdown post and saves its live screenshot to a specified location.\n\n
IMPORTANT! It needs to be run from the root of the Zola site.""",
        epilog="""
Examples:
    python social_cards_zola.py --base_url https://example.com --input content/blog/my_post.md --output_path static/img/social_cards
    python social_cards_zola.py -u -b http://127.0.0.1:1025 -i content/archive/_index.es.md -o static/img
    """,
    )
    parser.add_argument(
        "-b",
        "--base_url",
        default="http://127.0.0.1:1111",
        help="The base URL where the Zola site is hosted. Default is http://127.0.0.1:1111.",
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="""The relative path to the markdown file of the post/section you want to capture.
Should be in the format 'content/blog/post_name.language.md'.""",
    )
    parser.add_argument(
        "-o",
        "--output_path",
        required=True,
        help="The directory where the generated image will be saved.",
    )
    parser.add_argument(
        "-k",
        "--key",
        default="social_media_card",
        help="The front matter key to update. Default is 'social_media_card'.",
    )
    parser.add_argument(
        "-u",
        "--update-front-matter",
        action="store_true",
        help="Update or add the 'social_media_card' key in the front matter of the Markdown file.",
    )
    parser.add_argument(
        "-p",
        "--print_output",
        action="store_true",
        help="Print the path to the resulting screenshot at the end.",
    )
    return parser.parse_args()


def convert_filename_to_url(filename):
    # Remove .md extension
    post_name = os.path.splitext(filename)[0]

    # Remove "content/" prefix
    url = post_name.replace("content/", "", 1)

    # Extract language code
    parts = url.rsplit(".", 1)
    if len(parts) > 1 and len(parts[1]) == 2:
        lang_code = f"{parts[1]}/"
        url = parts[0]
    else:
        lang_code = ""

    # Handle co-located index.md by stripping it and using the directory as the URL
    if url.endswith("/index"):
        url = url.rsplit("/", 1)[0]

    # Remove "_index" suffix
    url = url.replace("_index", "")

    # Return the final URL with a single trailing slash
    full_url = f"{lang_code}{url}"
    return f"{full_url.rstrip('/')}/"


def error_exit(message, code=1):
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(code)


def validate_input_params(args):
    missing_params = []
    if not args.base_url:
        missing_params.append("base_url")
    if not args.input:
        missing_params.append("input")
    if not args.output_path:
        missing_params.append("output_path")

    if missing_params:
        error_exit(
            f"The following required settings are missing: {', '.join(missing_params)}. Use -h or --help for usage."
        )


def check_dependencies():
    try:
        import niquests
        from PIL import Image
    except ImportError as e:
        error_exit(f"Missing dependency: {e}. Please install it using pip.")

    if not shutil.which("shot-scraper"):
        error_exit("shot-scraper could not be found. Please install it.")


def fetch_status(base_url, post_url, max_retries=5):
    for _ in range(max_retries):
        try:
            response = niquests.head(f"{base_url}{post_url}", allow_redirects=True)
            if response.status_code == 200:
                return
        except niquests.RequestException:
            pass
        time.sleep(2)
    error_exit(
        f"Post {post_url} is not accessible. Max retries ({max_retries}) reached."
    )


def capture_screenshot(base_url, post_url):
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        temp_filename = temp_file.name

    try:
        subprocess.run(
            [
                "shot-scraper",
                "--silent",
                f"{base_url}/{post_url}",
                "-w",
                "700",
                "-h",
                "400",
                "--retina",
                "--quality",
                "60",
                "-o",
                temp_filename,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        error_exit(f"Failed to capture screenshot: {e.stderr}")

    return temp_filename


def move_file(temp_filename, output_path, post_url):
    safe_filename = re.sub(r"[^a-zA-Z0-9]", "_", post_url.rstrip("/"))
    safe_filename = safe_filename or "index"

    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    image_filename = output_path / f"{safe_filename}.jpg"

    # Convert PNG to JPG and save
    with Image.open(temp_filename) as img:
        img.convert("RGB").save(image_filename, "JPEG")

    os.unlink(temp_filename)
    return image_filename


def update_front_matter(md_file_path, image_output):
    with open(md_file_path, "r") as file:
        content = file.read()

    # Remove 'static/' from the beginning of the path if present
    image_output = str(image_output)
    if image_output.startswith("static/"):
        image_output = image_output[7:]

    front_matter_pattern = r"^\+\+\+\s*$(.*?)^\+\+\+\s*$"
    front_matter_match = re.search(
        front_matter_pattern, content, re.DOTALL | re.MULTILINE
    )

    if front_matter_match:
        front_matter = front_matter_match.group(1)
        extra_section = re.search(
            r"^\[extra\]\s*$(.*?)(\n\[|\Z)", front_matter, re.DOTALL | re.MULTILINE
        )

        if extra_section:
            # Update existing [extra] section
            updated_extra = re.sub(
                r"^social_media_card\s*=.*$",
                f'social_media_card = "{image_output}"',
                extra_section.group(1),
                flags=re.MULTILINE,
            )
            if "social_media_card" not in updated_extra:
                updated_extra += f'\nsocial_media_card = "{image_output}"'
            updated_front_matter = front_matter.replace(
                extra_section.group(1), updated_extra
            )
        else:
            # Add new [extra] section
            updated_front_matter = (
                front_matter + f'\n[extra]\nsocial_media_card = "{image_output}"\n'
            )

        updated_content = content.replace(
            front_matter_match.group(0), f"+++\n{updated_front_matter}+++"
        )
    else:
        # No front matter found, add it
        updated_content = (
            f'+++\n[extra]\nsocial_media_card = "{image_output}"\n+++\n\n{content}'
        )

    with open(md_file_path, "w") as file:
        file.write(updated_content)


def main():
    args = parse_arguments()
    validate_input_params(args)
    check_dependencies()

    args.base_url = args.base_url.rstrip("/") + "/"
    post_url = convert_filename_to_url(args.input)

    fetch_status(args.base_url, post_url)
    temp_filename = capture_screenshot(args.base_url, post_url)
    image_filename = move_file(temp_filename, args.output_path, post_url)

    if args.update_front_matter:
        update_front_matter(args.input, image_filename)

    if args.print_output:
        print(image_filename)


if __name__ == "__main__":
    main()
