+++
title = "Adapting Gilles Castel’s LaTeX Snippets for Typst"
description = "My attempt at converting Gilles Castel's LaTeX snippets to Typst on Neovim and VS Code to make writing math faster just like in Castel's original post."
date = 2023-10-07
updated = 2023-12-27
draft = true

[taxonomies]
tags = ["typst", "snippets", "vim", "neovim", "vscode"]

[extra]
# toc = true
# toc_ignore_pattern = "^(Table of Contents)"
# social_media_card = "https://2023.jskherman.com/blog/github-contributions/20210805-lottery-banner.jpg"
+++

{{ admonition(type="warning", text="There has been significant improvement in the programs, extensions, and plugins mentioned here since I last wrote this post. Some things don't apply anymore.") }}

1. [`typst.vim`][typst-vim] has been updated to support contexts, so the [caveat for the UltiSnips snippets](#caveats) is no longer needed.
2. I've added [LuaSnip] snippets for Typst as well. I decided to use LuaSnip now instead of UltiSnips since it's faster and more suitable for Neovim. Also, it's because I don't know what I'm doing with my Neovim config for UltiSnips and is a huge timesink.
3. Hypersnips snippets currently don't work with the Typst LSP, since the textmate scopes are not available again. There's an [open issue](https://github.com/nvarner/typst-lsp/issues/375) for this in the Typst LSP repo.

[LuaSnip]: https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md
[typst-vim]: https://github.com/kaarmu/typst.vim


1. [`typst.vim`][typst-vim] has been updated to support contexts, so the [caveat for the UltiSnips snippets](#caveats) is no longer needed.
2. I've added [LuaSnip] snippets for Typst as well. I decided to use LuaSnip now instead of UltiSnips since it's faster and more suitable for Neovim. Also, it's because I don't know what I'm doing with my Neovim config for UltiSnips and is a huge timesink.
3. Hypersnips snippets currently don't work with the Typst LSP, since the textmate scopes are not available again. There's an [open issue](https://github.com/nvarner/typst-lsp/issues/375) for this in the Typst LSP repo.

[LuaSnip]: https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md
[typst-vim]: https://github.com/kaarmu/typst.vim


~~Recently, I noticed that the [VS Code extension for the Typst LSP][typst-lsp] added support for `textmate scopes`, which means that I can now use [HyperSnips] snippets for my [Typst] files![^1]~~ On another note, there's also a [proof-of-concept support][typst-vim-51] for contexts with the [`typst.vim`](https://github.com/kaarmu/typst.vim) plugin in Neovim, just like in the [`vimtex plugin`][vimtex]. Now making it possible to have [UltiSnips] work with Typst files as well.

Seeing as writing snippets for Typst is now possible with Neovim and/or VS Code. I set out last night to convert some of the snippets in [Gilles Castel's original blog post on his LaTeX snippets][castel-post] that I found useful for my own use.

## Links

> The Typst snippets I made are available in my [dotfiles repository][dotfiles-repo]:
> - [HyperSnips snippets][dotfiles-repo-hsnips][^4]
> - [UltiSnips snippets][dotfiles-repo-ultisnips][^5]
> - [LuaSnip snippets][dotfiles-repo-luasnips]

## Caveats

~~A caveat though to using the UltiSnips snippets in [Neo]vim is that the [`typst.vim` plugin](https://github.com/kaarmu/typst.vim) installation must be tied to commit `96f58d5`[^2].~~

On the other hand, the caveat for the HyperSnips snippets is that there is no such thing as a "`VISUAL`" mode in VS Code, so the snippets that rely on it won't work. To work around this, I used [a suggested solution in the HyperSnips repo][visual-workaround] making use of the VS Code API which replaces the `VISUAL` mode with TextMate's `TM_SELECTED_TEXT` variable.[^3]

<!-- Links -->

[typst-lsp]: https://marketplace.visualstudio.com/items?itemName=nvarner.typst-lsp
[HyperSnips]: https://marketplace.visualstudio.com/items?itemName=draivin.hsnips
[Typst]: https://typst.app
[typst-vim-51]: https://github.com/kaarmu/typst.vim/commit/96f58d513b5e23ce1313e061fbab61cd7f3b4e3f
[vimtex]: https://github.com/lervag/vimtex
[UltiSnips]: https://github.com/SirVer/ultisnips
[castel-post]: https://castel.dev/post/lecture-notes-1/
[dotfiles-repo]: https://github.com/jskherman/dotfiles
[dotfiles-repo-hsnips]: https://github.com/jskherman/dotfiles/blob/4d6d95a249d68c7ebc4b104375b04c53a42e9987/hsnips/typst.hsnips
[dotfiles-repo-ultisnips]: https://github.com/jskherman/dotfiles/blob/4d6d95a249d68c7ebc4b104375b04c53a42e9987/nvim/UltiSnips/typst.snippets
[dotfiles-repo-luasnips]: https://github.com/jskherman/dotfiles/blob/f9baad3312f1ad3f0f294420a47dadbce73693f0/nvim/LuaSnip/typst.lua
[visual-workaround]: https://github.com/draivin/hsnips/issues/81#issuecomment-970168548

<!-- Footnotes -->

[^1]: HyperSnips is a snippet engine for VS Code heavily inspired by vim's [UltiSnips].
[^2]: At least until it's implemented in the main branch of the `typst.vim` plugin.
[^3]: An example is [this snippet](https://github.com/jskherman/dotfiles/blob/4d6d95a249d68c7ebc4b104375b04c53a42e9987/hsnips/typst.hsnips#L391-L394) which surrounds selected text with parentheses.
[^4]: Currently unusable, because of the lack of TextMate scopes in the Typst LSP still.
[^5]: I don't use Ultisnips anymore, see [LuaSnip](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md)
