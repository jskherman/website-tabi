+++
title = "Migrating my website *again* for the fifth time"
description = "Lessons I learned in my journey of migrating my website four times, encountering template issues, and exploring various themes and site generators."
date = 2023-05-24
updated = 2024-04-27
draft = true

[taxonomies]
tags = ["blogging", "websites", "data", "static site generators", "hugo", "zola"]
+++

I just finished migrating my website **again for the _fourth_ time**. Yay! 🎉

The migration this time was driven by my inability to build my Hugo website using the [Stack theme by @CaiJimmy](https://github.com/CaiJimmy/hugo-theme-stack) because for some reason it cannot fetch the site templates for some pages. It probably has something to do with how the theme is distributed over Hugo modules and on GitHub since I cannot fetch the theme's templates via the Hugo module method or the Git submodule method. With this, all that I'm left with is a site that cannot build and a previously deployed version on Netlify.

This is the *first time* I have been alerted to the risk to Hugo websites regarding this [template issue](https://github.com/CaiJimmy/hugo-theme-stack/issues/815#issue-1689445412). And this seems to be a common risk shared by all sites generated using Hugo from an externally developed theme. The probability of me encountering this risk again seems small but still possible.

On a side note, the last three Hugo migrations I did was because I did not fancy the style, nor the features associated with the theme I selected for long enough. The last three themes I tried was [@dsrkafuu's Fuji theme](https://github.com/dsrkafuu/hugo-theme-fuji), [@dillonzq's LoveIt theme](https://github.com/dillonzq/LoveIt), and [@adityatelange's PaperMod theme](https://github.com/adityatelange/hugo-PaperMod). In the past before I knew/decided to use Hugo, I also tinkered with Jekyll themes, Gatsby and Next.js site templates, and even tried out WordPress using a DigitalOcean droplet and Namecheap's (paid) hosting at first when I was learning how websites were deployed and how they worked.

Looking back, there was always something that I eventually discovered and learned about that would compel me to seek a better setup. It felt like when I started learning programming all over again. There was always the question of what the best choice is to make here. Instead of just getting started, I kept getting sidetracked trying to make the experience of my personal website better and suited to my tastes — i.e., shiny object syndrome (SOS).

On that note though, I did not regret learning about static site generators (SSG). I went from paying 5 or 6 USD/month for WordPress hosting to <mark>**_absolutely free_**</mark> (as in free beer) static site hosting. What I have is a personal blog. *It's not a website of a large corporation*  with millions of visitors every day. Hosting this should be inexpensive.[^1][^2] In terms of possible costs saved, this is a HUGE win.

In hindsight, it was probably inevitable since I was largely ignorant of what's possible to achieve with websites. *It's mind-bogglingly complex*... **and I haven't even touched JavaScript or Node.js yet!**

Who knows if I will settle with my currently chosen theme of [@reorx's PaperModX theme](https://github.com/reorx/hugo-PaperModX/) (a fork of the earlier [@adityatelange's PaperMod theme](https://github.com/adityatelange/hugo-PaperMod))? So far it seems good enough for what I need currently. Maybe this time, I'll add functionality myself instead of relying so much on the pre-made theme's features out-of-the-box.

---

`2024-04-26` **UPDATE**: I moved to using [Zola](https://getzola.org/) over Hugo. The Tera templating seems easier to read and work with than Go's templating in Hugo. The new theme I settled on is [@welpo's tabi theme](https://github.com/welpo/tabi). Some of the shortcodes I used in PaperModX were already implemented plus a few more bonus shortcodes. The theme also by default uses Inter for the sans-serf font, Source Serif 4 as the serif font, and Cascadia Code for the monospace font which I was thinking.

Moving forward, I'll archive past website iterations in subdomains of jskherman.com such as [2023.jskherman.com](https://2023.jskherman.com) and [2024.jskherman.com](https://2024.jskherman.com). I highly doubt I'll be migrating my website again more than once in a year so this seems fine for now. Even if I did have multiple iterations, I'll just choose the definitve iteration to have the year subdomain.

ฅ⁠^⁠•⁠ﻌ⁠•⁠^⁠ฅ

<!-- footnotes -->

[^1]: I'm grateful that services like [Netlify](https://netlify.com), [Vercel](https://vercel.com), [Cloudflare Pages](https://pages.cloudflare.com), [GitHub Pages](https://pages.github.com), and [Surge.sh](https://surge.sh) exist. They make it possible for something amazing like hosting a website for free to be possible for students like me.

[^2]: You do have to be careful with platforms like Netlify or Vercel because [**they will charge you _a lot_**](https://old.reddit.com/r/webdev/comments/1b14bty/netlify_just_sent_me_a_104k_bill_for_a_simple/) if you exceed their free tier limits, especially when you can be DDoSed or have your site be popular overnight. Since this site is just a personal blog, I don't want to be charged for something that I don't make money from and I would want this site to be down instead of me paying for it to be up in such an event.
