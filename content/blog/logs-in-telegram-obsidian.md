+++
title = "Interstitial journaling with Telegram and Obsidian"
date = 2024-02-20
# updated = 2024-05-06
draft = false

[taxonomies]
tags = ["journaling", "telegram", "plaintext", "obsidian", "μ"]

[extra]
giscus = true
+++

I recently discovered the [Telegram Sync](https://github.com/soberhacker/obsidian-telegram-sync) plugin for Obsidian, which allows me to seamlessly transfer messages from Telegram to a file of my choice in my Obsidian Vault. I've set it up to append new messages under the `## Log` heading in my daily note for the current day.

To make this workflow efficient, I've also configured my daily note to automatically create a `## Log` heading upon creation, along with Obsidian opening (and creating, if necessary) the daily note upon startup. This integration eliminates the need to choose between Telegram for quick capture and Obsidian for long-form writing and data ownership. I can now enjoy the best of both worlds.


Here's an example of how a daily note would look like:

```markdown
... other daily note content

## Log

`15:18` Nec dubitamus multa iter quae et nos invenerat.

`19:30` Lorem ipsum dolor sit amet.
```

The template I'm using automatically adds a timestamp in `HH:mm` format at the start of each message. While I still need to test the template's compatibility with images and other files sent via Telegram, it's not a priority for me since I rarely take pictures.


