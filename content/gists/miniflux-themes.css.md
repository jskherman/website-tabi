+++
title = "📋miniflux-themes.css"
description = "A collection of themes for Miniflux (RSS Reader)."
date = 2024-04-30
draft = false

[taxonomies]
tags = ["rss", "css", "design"]

[extra]
# social_media_card = ""
+++

Some themes for [Miniflux (RSS Reader)](https://github.com/miniflux/v2).

Below is a theme that has a few tweaks of the default sans-serif theme.

```css
/* Need to allow api.fonts.coollabs.io in Content Security Policy */
/* @import url('https://api.fonts.coollabs.io/css2?family=IBM+Plex+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,200..900&display=swap'); */

:root {
    --red: #f38ba8;
    --orange: #fab387;
    --green: #a6e3a1;
    --light-blue: #74c7ec;
    --blue: #77bdfb;
    --purple: #cea5fb;
    --sans-serif: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !important;
    --serif: "Source Serif 4", Georgia, "Times New Roman", Times, serif;
}

.entry-content {
    font-size: 1em;
}

.item {
    border: none;
}

.logo a {
    font-weight: 600;
}

nav {
    font-family: var(--sans-serif);
}

:root {
    --font-family: var(--serif);
    --entry-content-font-family: var(--sans-serif);
    --entry-content-font-weight: 400;
    /* Light */
    --entry-content-color: #424242;
    /* Dark */
    /* --entry-content-color: #D3D3D3; */
}
```

---

A longer version tweaked from [the original](https://revcd.com/applying-github-dark-theme-miniflux-gpt) based on the GitHub Dark theme.

```css
/* Need to allow api.fonts.coollabs.io in Content Security Policy */
/* @import url('https://api.fonts.coollabs.io/css2?family=IBM+Plex+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,200..900&display=swap'); */
/* @import url('https://api.fonts.coollabs.io/css2?family=Fira+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,200..900&display=swap'); */

:root {
    --base0: #1e1e2e;
    --base1: #363654;
    --base2: #4e4e7a;
    --base3: #bac2de;
    --base4: #cdd6f4;
    --base5: #ecf2f8;
    --red: #f38ba8;
    --orange: #fab387;
    --green: #a6e3a1;
    --light-blue: #74c7ec;
    --blue: #77bdfb;
    --purple: #cea5fb;
    --sans-serif: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !important;
    --serif: "Source Serif 4", Georgia, "Times New Roman", Times, serif;
}

.logo a span {
    color: var(--orange) !important;
}

.entry-content {
    font-size: 1em;
}

.item {
    border: none;
}

:root {
    --font-family: var(--sans-serif);
    --entry-content-font-family: var(--serif);
    --entry-content-font-weight: 400;
    --item-status-read-title-link-color: var(--link-color);
    --body-color: var(--base5);
    --body-background: var(--base0);
    --hr-border-color: var(--base2);
    --title-color: var(--light-blue);
    --link-color: var(--base5);
    --link-focus-color: var(--base4);
    --link-hover-color: var(--base3);
    --link-visited-color: var(--base4);
    --header-list-border-color: var(--base2);
    --header-link-color: var(--base5);
    --header-link-focus-color: var(--base4);
    --header-link-hover-color: var(--base3);
    --header-active-link-color: var(--light-blue);
    --table-border-color: var(--base2);
    --table-th-background: var(--base1);
    --table-th-color: var(--base5);
    --table-tr-hover-background-color: var(--base2);
    --table-tr-hover-color: var(--base5);
    --button-primary-border-color: var(--green);
    --button-primary-background: var(--green);
    --button-primary-color: var(--base0);
    --button-primary-focus-border-color: var(--base2);
    --button-primary-focus-background: var(--base2);
    --input-background: var(--base1);
    --input-color: var(--base5);
    --input-placeholder-color: var(--base3);
    --input-focus-color: var(--base5);
    --input-focus-border-color: var(--blue);
    --input-focus-box-shadow: 0 0 0 2px var(--base2);
    --alert-color: var(--base5);
    --alert-background-color: var(--base0);
    --alert-border-color: var(--base2);
    --alert-success-color: var(--base0);
    --alert-success-background-color: var(--green);
    --alert-success-border-color: var(--base2);
    --alert-error-color: var(--base5);
    --alert-error-background-color: var(--red);
    --alert-error-border-color: var(--base2);
    --alert-info-color: var(--base5);
    --alert-info-background-color: var(--base2);
    --alert-info-border-color: var(--base2);
    --page-header-title-border-color: var(--base2);
    --logo-color: var(--light-blue);
    --logo-hover-color-span: var(--blue);
    --panel-background: var(--base1);
    --panel-border-color: var(--base2);
    --panel-color: var(--base5);
    --modal-background: var(--base0);
    --modal-color: var(--base5);
    --modal-box-shadow: 2px 0 5px 0 var(--base2);
    --pagination-link-color: var(--base5);
    --pagination-border-color: var(--base2);
    --category-color: var(--base5);
    --category-background-color: var(--base2);
    --category-border-color: var(--base2);
    --category-link-color: var(--base5);
    --category-link-hover-color: var(--light-blue);
    --item-border-color: var(--base2);
    --item-status-read-title-link-color: var(--light-blue);
    --item-status-read-title-focus-color: var(--base4);
    --item-meta-focus-color: var(--base4);
    --item-meta-li-color: var(--base5);
    --current-item-border-color: var(--blue);
    --entry-header-border-color: var(--base2);
    --entry-header-title-link-color: var(--base5);
    --entry-content-color: var(--base5);
    --entry-content-code-color: var(--light-blue);
    --entry-content-code-background: var(--base1);
    --entry-content-code-border-color: var(--base2);
    --entry-content-quote-color: var(--base4);
    --entry-content-abbr-border-color: var(--base2);
    --entry-enclosure-border-color: var(--base2);
    --parsing-error-color: var(--base5);
    --feed-parsing-error-background-color: var(--red);
    --feed-parsing-error-border-color: var(--base2);
    --feed-has-unread-background-color: var(--green);
    --feed-has-unread-border-color: var(--base2);
    --category-has-unread-background-color: var(--green);
    --category-has-unread-border-color: var(--base2);
    --keyboard-shortcuts-li-color: var(--base5);
    --counter-color: var(--base5);
}
```
