+++
title = "📋statuscafe_parser.py"
description = "A Python script that parses an Atom RSS feed from status.cafe and exports the data to a CSV file."
date = 2024-03-08
# updated = 2024-04-25
draft = false

[taxonomies]
tags = ["python", "scripting", "csv", "data extraction"]

[extra]
+++

A Python script that parses an Atom RSS feed from status.cafe and exports the data to a CSV file

```python
# =============================================================================
#
# Author: jskherman
# Date: 2024-03-08
# Description:
#   This script parses an XML file from status.cafe in the Atom format, which
#   typically represents an RSS feed. The script extracts relevant information
#   from the entries in the feed, such as the title, author, published
#   timestamp, content, ID, and link. It then processes this information and
#   writes it to a CSV file.
#
#   Specifically, the script performs the following tasks:
#
#   1. Prompts the user to enter the name of the XML file to parse.
#   2. Parses the provided XML file using the xml.etree.ElementTree module.
#   3. Extracts the following information from each entry in the feed:
#      - Title
#      - Author
#      - Published timestamp (converted to a UNIX timestamp)
#      - Content (with HTML entities decoded)
#      - ID (extracted from the URL in the 'id' node)
#      - Link (for the 'alternate' link)
#      - Emoji (extracted from the title, assuming it's the second word)
#   4. Checks for duplicate IDs in the feed entries. If any duplicates are
#      found, it raises a ValueError with the duplicate IDs and their
#      corresponding status updates.
#   5. Writes the extracted information to a CSV file named 'output.csv',
#      with the following columns:
#      - ID
#      - Timestamp
#      - Author
#      - Emoji
#      - Status
#      - Link
#   6. Prints a success message if the execution is successful.
#   7. If an exception occurs during execution, it prints the error message.
#
# Dependencies:
#   - xml.etree.ElementTree: for parsing the XML file
#   - csv: for writing the data to a CSV file
#   - html: for decoding HTML entities in the content
#   - re: for using regular expressions to extract the ID from the URL
#   - datetime: for converting the timestamp string to a UNIX timestamp
#
# Usage:
#   1. Save this script to a file (e.g., feedparser.py).
#   2. Run the script using the Python interpreter: `python feedparser.py`
#   3. When prompted, enter the name of the XML file to parse (e.g., feed.xml).
#   4. The script will process the file and generate an 'output.csv' file in
#      the same directory.
#   5. If any errors occur, the script will print the error message and provide
#      helpful information.
#
# =============================================================================

import xml.etree.ElementTree as ET
import csv
from html import unescape
import re
from datetime import datetime, timezone

def extract_emoji(title):
    """
    Extract the emoji from the title string.

    Args:
        title (str): The title string from which to extract the emoji.

    Returns:
        str: The extracted emoji, or an empty string if no emoji is found.
    """
    # Split the title by whitespace
    title_parts = title.split()

    # Get the second element as the emoji
    if len(title_parts) > 1:
        return title_parts[1]
    else:
        return ""

def get_status_id(id_url):
    """
    Extract the status ID from the given URL.

    Args:
        id_url (str): The URL containing the status ID.

    Returns:
        str: The extracted status ID, or an empty string if no ID is found.
    """
    # Extract the digits at the end of the URL
    match = re.search(r"/(\d+)$", id_url)
    if match:
        return match.group(1)
    else:
        return ""

def main():
    try:
        # Ask the user for the file name
        file_name = input("Enter the name of the file to parse: ")

        # Parse the XML file
        tree = ET.parse(file_name)
        root = tree.getroot()

        # Open a CSV file for writing
        with open("output.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "ID",
                "Timestamp",
                "Author",
                "Emoji",
                "Status",
                "Link",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row in the CSV file
            writer.writeheader()

            # Initialize a set to store unique IDs
            unique_ids = set()
            # Initialize a dictionary to store duplicate IDs and their corresponding status updates
            duplicate_ids = {}

            # Iterate over the entries in the XML file
            for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
                title = entry.find("{http://www.w3.org/2005/Atom}title").text
                author = entry.find(
                    "{http://www.w3.org/2005/Atom}author/{http://www.w3.org/2005/Atom}name"
                ).text
                timestamp_str = entry.find(
                    "{http://www.w3.org/2005/Atom}published"
                ).text
                # Convert the timestamp string to a UNIX timestamp
                timestamp = int(
                    datetime.fromisoformat(
                        timestamp_str.replace("Z", "+00:00")
                    ).timestamp()
                )
                content = unescape(
                    entry.find("{http://www.w3.org/2005/Atom}content").text
                )
                id_url = entry.find("{http://www.w3.org/2005/Atom}id").text
                status_id = get_status_id(id_url)
                link = entry.find('{http://www.w3.org/2005/Atom}link[@rel="alternate"]')
                if link is not None:
                    link = link.attrib["href"]
                else:
                    link = ""

                emoji_mood = extract_emoji(title)

                # Check if the ID is already in the set
                if status_id in unique_ids:
                    # If it's a duplicate, store it in the duplicate_ids dictionary
                    duplicate_ids[status_id] = content
                else:
                    # If it's a unique ID, add it to the set and write the row to the CSV
                    unique_ids.add(status_id)
                    writer.writerow(
                        {
                            "ID": status_id,
                            "Timestamp": timestamp,
                            "Author": author,
                            "Emoji": emoji_mood,
                            "Status": content,
                            "Link": link,
                        }
                    )

            # Check if there were any duplicate IDs
            if duplicate_ids:
                # Raise an error with the duplicate IDs and their corresponding status updates
                duplicate_ids_str = "\n".join(
                    [
                        f"ID: {id}, Status: {duplicate_ids[id]}"
                        for id in duplicate_ids
                    ]
                )
                raise ValueError(
                    f"Duplicate IDs found in the input file:\n{duplicate_ids_str}"
                )

        print("Execution successful! CSV file 'output.csv' has been created.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure that the file you provided is a valid XML file.")

if __name__ == "__main__":
    main()
```
