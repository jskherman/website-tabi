+++
title = "Applying multiple variable transforms in VS Code snippets"
description = "Figuring out how to apply multiple transforms to a variable in VS Code snippets using RegEx capture groups."
date = 2023-05-24
draft = false

[taxonomies]
tags = ["vs code", "snippets", "regex", "templates", "TIL"]

[extra]
# toc = true
# toc_ignore_pattern = "^(Table of Contents)"
# social_media_card = "https://2023.jskherman.com/blog/github-contributions/20210805-lottery-banner.jpg"
+++

{{ admonition(type="info", title="TL;DR", text="It might not be possible. But there are workarounds via [capture groups](https://stackoverflow.com/a/66508882).") }}

Today I learned how to apply multiple transforms to a variable in VS Code snippets using RegEx capture groups. I was trying to create a VS Code snippet for quickly creating new markdown files with prefilled [Hugo](https://gohugo.io/) post metadata fields. I wanted to be able to type `@note` and have it expand to the following (using an example filename):

```markdown
<!-- Filename: 2023-05-24_example-post-1.md -->
---
slug: example-post-1
title: Example Post 1
date: 2023-05-24T16:47:35+08:00
tags: []
---

your text here
```

## Setting up the snippet

I was able to get the ISO timestamp easily as well as tabstops for the `tags` field and body of the post by following the [documentation for VS Code snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_variables). So far, I got the following:

```json
{
    "SITREP": {
        "scope": "md, markdown",
        "prefix": "@note",
        "body": [
            "---",
            "slug: ",
            "title: ",
            "date: ${CURRENT_YEAR}-${CURRENT_MONTH}-${CURRENT_DATE}T${CURRENT_HOUR}:${CURRENT_MINUTE}:${CURRENT_SECOND}+08:00",
            "tags: [$1]",
            "---",
            "",
            "$0"
        ],
        "description": "Create a new post"
    }
}
```

## Transform: extracting the slug with RegEx

The next step now is figuring out how to extract the `slug` from the filename of my markdown file, which is `example-post-1` from `2023-05-24_example-post-1.md`. Diving into the documentation again, I saw that [variable transforms](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_transform-examples) would be able to do it. After a while of tinkering, I got it to work:

```json,linenostart=5,hl_lines=5
{
    // ...
    "body": [
        "---",
        "slug: ${TM_FILENAME_BASE/^(\\d{4}-\\d{2}-\\d{2})_(.*)/$2/}",
        "title: ",
        "date: ${CURRENT_YEAR}-${CURRENT_MONTH}-${CURRENT_DATE}T${CURRENT_HOUR}:${CURRENT_MINUTE}:${CURRENT_SECOND}+08:00",
        "tags: [$1]",
        "---",
        "",
        "$0"
    ],
    // ...
}
```

Now that is out of the way, it's time to deal with the `title` field next. Surely, I can just use the same RegEx transform and add some additional rules to create the title from the filename, right? It will be just that simple, right? *Nope.*

![Anakin Padme Meme about variable transforms](https://2023.jskherman.com/blog/vscode-var-transform-snippets/anakin-padme-var-transform-meme.png)

## Transform: extracting the title with RegEx

After countless tries I had with the documentation, it's time to bring in some help from StackOverflow. I found that someone had a similar problem to mine. They wanted to extract the title from a filename `test-file-name.md`, and end up with `Test File Name` as the output of their snippet. The [StackOverflow solution](https://stackoverflow.com/a/66508882) was to use the RegEx transform <span>`/([^-]+)(-*)/g`</span> in the snippet:

```json
{
    "body": "${TM_FILENAME_BASE/([^-]+)(-*)/${1:/capitalize}${2:+ }/g}"
}
```

> "...Because of the `g` flag it will get all the occurrences and do each transform of the two capture groups multiple time. In your test case `(test-)(file-)(name)` that would be three times. It should work for any number of hyphenated words.
>
> `([^-]+)` everything up to a hyphen.
>
> `${1:/capitalize}` capitalize capture group 1.
>
> `${2:+ }` means if there is a 2nd capture group, the `(-*)`, add a space. I added this because at the end there is no hyphen - and thus there will be no 2nd capture group and thus no extra space should be added at the end."
>
> —[<cite>Mark (StackOverflow)</cite>](https://stackoverflow.com/a/66508882)

However this did not work for me since I have a `YYYY-MM-DD` date in front plus an underscore to be mindful of: `2023-05-24_example-post-1.md`.

After tinkering for a while again, I decided to just use another capture group to capture my prefix of `2023-05-24_` and ignore that capture group in the transform. Since there were three capture groups, I had to increment the integers in the original solution by one. The solutions seems to also work with symbols as well. The regex and snippet look like these:

```regex
(\\d{4}-\\d{2}-\\d{2}_)|([^-]+)(-*)
```

```json
{
    "body": "title: ${TM_FILENAME_BASE/(\\d{4}-\\d{2}-\\d{2}_)|([^-]+)(-*)/${2:/capitalize}${3:+ }/g}"
}
```

Therefore, the final snippet overall is as follows:

```json
{
    "SITREP": {
        "scope": "md, markdown",
        "prefix": "@sitrep",
        "body": [
            "---",
            "slug: ${TM_FILENAME_BASE/^(\\d{4}-\\d{2}-\\d{2})_(.*)/$2/}",
            "title: ${TM_FILENAME_BASE/(\\d{4}-\\d{2}-\\d{2}_)|([^-]+)(-*)/${2:/capitalize}${3:+ }/g}",
            "date: ${CURRENT_YEAR}-${CURRENT_MONTH}-${CURRENT_DATE}T${CURRENT_HOUR}:${CURRENT_MINUTE}:${CURRENT_SECOND}+08:00",
            "tags: [$1]",
            "---",
            "",
            "$0"
        ],
        "description": "Create a new post"
    }
}
```

## Conclusion

I do not know if there is a better way to do this rather than to use capture groups, but this is the best I could come up with. I'm not sure if there really is a way to chain multiple transforms to a variable in VS Code Snippets, but I'm glad that I was able to find a workaround. I hope this helps someone else out there who is trying to do something similar.
