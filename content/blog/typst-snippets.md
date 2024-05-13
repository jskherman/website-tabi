+++
title = "Adapting Gilles Castel’s LaTeX snippets for Typst"
description = "My attempt at converting Gilles Castel's LaTeX snippets to Typst on Neovim and VS Code to make writing math faster just like in Castel's original post."
date = 2023-10-07
updated = 2023-12-27
draft = false

[taxonomies]
tags = ["typst", "snippets", "vim", "neovim", "vs code"]

[extra]
katex = true
giscus = true
# toc = true
# toc_ignore_pattern = "^(Table of Contents)"
# social_media_card = "https://2023.jskherman.com/blog/github-contributions/20210805-lottery-banner.jpg"
+++



~~Recently,~~ I noticed that the [VS Code extension for the Typst LSP](https://marketplace.visualstudio.com/items?itemName=nvarner.typst-lsp) added support for `textmate scopes`, which means that I can now use [HyperSnips](https://marketplace.visualstudio.com/items?itemName=draivin.hsnips) snippets for my [Typst](https://typst.app) files! [^1] On another note, there's also support now for contexts with the [`typst.vim`](https://github.com/kaarmu/typst.vim) plugin in Neovim, just like in the [`vimtex plugin`](https://github.com/lervag/vimtex). Now making it possible to have [UltiSnips](https://github.com/SirVer/ultisnips) and [LuaSnip](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md) work with Typst files as well.

Seeing as writing snippets for Typst is now possible with Neovim and/or VS Code. I set out last night to convert some of the snippets in [Gilles Castel's original blog post on his LaTeX snippets](https://castel.dev/post/lecture-notes-1/) that I found useful for my own use.

In the process of porting over the snippets from $\LaTeX$ to Typst, a lot of the snippets in Castel's post are not applicable anymore just because [Typst's syntax](https://typst.app/docs/guides/guide-for-latex-users) is far easier, brief, and more convenient to write. For example, the fraction snippet in $\LaTeX$ which involves using `/` and regex in order to transform the `1/2` way of writing fractions into proper $\LaTeX$ syntax is no longer necessary in Typst because fractions are now just `1/2` in Typst literally.[^2]

## Links

> These snippets are hacky and unpolished. They're provided as is so use them at your own risk. The Typst snippets I made are available in my [dotfiles repository](https://github.com/jskherman/dotfiles):
>
> - [HyperSnips snippets](https://github.com/jskherman/dotfiles/blob/4d6d95a249d68c7ebc4b104375b04c53a42e9987/hsnips/typst.hsnips)[^3]
> - [UltiSnips snippets](https://github.com/jskherman/dotfiles/blob/4d6d95a249d68c7ebc4b104375b04c53a42e9987/nvim/UltiSnips/typst.snippets)[^4]
> - [LuaSnip snippets](https://github.com/jskherman/dotfiles/blob/f9baad3312f1ad3f0f294420a47dadbce73693f0/nvim/LuaSnip/typst.lua)

## Caveats

A caveat for the HyperSnips snippets is that there is no such thing as a "`VISUAL`" mode in VS Code like in Vim/Neovim, so the snippets that rely on it won't work. To work around this, I used [a suggested solution in the HyperSnips repo](https://github.com/draivin/hsnips/issues/81#issuecomment-970168548) which makes use of the VS Code API which replaces the `VISUAL` mode with TextMate's `TM_SELECTED_TEXT` variable.[^5]

<!-- Footnotes -->

[^1]: HyperSnips is a snippet engine for VS Code heavily inspired by vim's [UltiSnips](https://github.com/SirVer/ultisnips).

[^2]: Scoping is also done, as you would expect, with parentheses which is good and a lot like written math instead of numerous curly brackets.

[^3]: These snippets require some reworking in order to work with the updates to the Typst LSP in VS Code.

[^4]: I don't use Ultisnips anymore, see [LuaSnip](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md).

[^5]: An example is [this snippet](https://github.com/jskherman/dotfiles/blob/4d6d95a249d68c7ebc4b104375b04c53a42e9987/hsnips/typst.hsnips#L391-L394) which surrounds selected text with parentheses.

