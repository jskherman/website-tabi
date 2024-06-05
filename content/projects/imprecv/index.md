+++
title = "imprecv"
description = "A no-frills CV template using Typst and YAML to version control CV data."
weight = 10

[extra]
local_image = "projects/imprecv/cv_thumbnail.png"
# social_media_card = "social_cards/projects_doteki.jpg"
canonical_url = "https://www.jskherman.com/projects/imprecv/"
+++


`imprecv` is a no-frills curriculum vitae (CV) template for [Typst](https://github.com/typst/typst) that uses a YAML file for data input in order to version control CV data easily.

This is based on the [popular template on Reddit](https://web.archive.org/https://old.reddit.com/r/jobs/comments/7y8k6p/im_an_exrecruiter_for_some_of_the_top_companies/) by [u/SheetsGiggles](https://web.archive.org/https://old.reddit.com/user/SheetsGiggles) and the recommendations of the [r/EngineeringResumes wiki](https://web.archive.org/https://old.reddit.com/r/EngineeringResumes/comments/m2cc65/new_and_improved_wiki).

<details><summary>See <strong><a href="https://github.com/jskherman/imprecv/releases/latest/download/example.pdf" target="_blank">example CV</a></strong> and <a href="https://go.jskherman.com/cv">@jskherman's CV</a>.
</summary>

{{ image_toggler(default_src="https://github.com/jskherman/imprecv/raw/main/assets/thumbnail.1.png", toggled_src="https://github.com/jskherman/imprecv/raw/main/assets/thumbnail.2.png", default_alt="Sample CV page 1", toggled_alt="Sample CV page 1") }}

</details>

#### [GitHub](https://github.com/jskherman/imprecv) • [Typst Universe](https://typst.app/universe/package/imprecv) {.centered-text}

## Usage

This `imprecv` is intended to be used by importing the template's [package entrypoint](cv.typ) from a "content" file (see [`template.typ`](template/template.typ) as an example).
In this content file, call the functions which apply document styles, show CV components, and load CV data from a YAML file (see [`template.yml`](template/template.yml) as an example).
Inside the content file you can modify several style variables and even override existing function implementations to your own needs and preferences.

### With the [Typst CLI](https://github.com/typst/typst)

The recommended usage with the [Typst CLI](https://github.com/typst/typst) is by running the command `typst init @preview/imprecv:1.0.0` in your project directory.
This will create a new Typst project with the `imprecv` template and the necessary files to get started.
You can then run `typst compile template.typ` to compile your file to PDF.

Take a look at the [example setup](https://github.com/jskherman/cv.typ-example-repo) for ideas on how to get started. It includes a GitHub action workflow to compile the Typst files to PDF and upload it to Cloudflare R2.

### With [typst.app](https://typst.app)

From the Dashboard, select "Start from template", search and choose the `imprecv` template.
From there, decide on a name for your project and click "Create".
You can now edit the template files and preview the result on the right.

You can also click the `Create project in app` button in [Typst Universe](https://typst.app/universe/package/imprecv) to create a new project with the `imprecv` template.

[![Star History Chart](https://api.star-history.com/svg?repos=jskherman/imprecv&type=Date)](https://star-history.com/#jskherman/imprecv&Date)

