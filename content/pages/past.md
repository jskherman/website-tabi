+++
title = "The Past"
template = "info-page.html"
path = "past"
date = 2021-06-21
updated = 2024-06-05 

[extra]
katex = true
quick_navigation_buttons = true
+++

{% admonition(type="info") %}

<details><summary>Show Table of Contents</summary><!-- toc --></details>
{% end %}

<!-- ## The Year 2024 -->

## The Year 2023

### December


+ `2023-12-04` I have switched over my quantified self site to use [Holoviz's Panel library](https://panel.holoviz.org) to create the dashboards. I'm planning to add more data sources and pages to it when I have free time. I currently have on there a page tracking how much time I have spent studying for the Chemical Engineering board exam.

+ `2023-12-05` I'm currently working on adjusting my body clock to wake up earlier for the review. I found that it was easier to do in a new environment than when I was at home, despite both places of sleep having no access to sunlight.

+ `2023-12-15` Working on some small tweaks/fixes on the side for my [résumé/CV template](https://github.com/jskherman/cv.typ) made with $\ \xcancel{\LaTeX} \ $ [Typst](https://typst.app). I sometimes find myself checking the repository to see if it has reached 100 stars yet. It's currently at 97 stars on `2023-12-27`. Imaginary internet points, lol. It got featured on Twitter by the [Typst team](https://twitter.com/typstapp), which made me a bit enthused.
  > Let's start with the classics: Try [@jskherman](https://twitter.com/jskherman?ref_src=twsrc%5Etfw)'s template if you are a after a classy, evergreen look <https://github.com/jskherman/cv.typ>
  >
  > <details><summary>Preview</summary>{{ image_toggler(default_src="https://github.com/jskherman/imprecv/raw/main/assets/thumbnail.1.png", toggled_src="https://github.com/jskherman/imprecv/raw/main/assets/thumbnail.2.png", default_alt="Page 1 Template Preview", toggled_alt="Page 2 Template Preview") }}</details>
  >
  > &mdash; Typst (@typstapp) [December 21, 2023](https://twitter.com/typstapp/status/1737806834000441835?ref_src=twsrc%5Etfw)


### July

+ `2023-07-01` Just graduated as Cum Laude with a degree of Bachelor of Science in Chemical Engineering. Right now, I am preparing for the board exams for Chemical Engineering. I still have a lot of things to do and this was not the rest I was hoping after graduating. Life happens I guess.
  + While procrastinating I created a [quick prototype of a problem set generator](https://github.com/jskherman/che-pset) to help me study for the board exams. I'm still thinking of how to improve it and make it more useful for other people. I may or may not be thinking of how to monetize it. Most of the technical work is done, it's just gathering the questions and answers that is the hard part.
  + I also created a [curriculum vitae/résumé template](https://go.jskherman.com/cv) in ~~$\LaTeX$~~ Typst so that I can easily update my CV in the future. I made it so that I can easily put my resume under version control with Git. I also made it available for others to use and you can [download the template on GitHub here](https://github.com/jskherman/cv.typ).
  + On the background, I was trying a lot of self-hosted solutions on the [Fly.io](https://fly.io) platform. I currently have the following deployed:
    + A web app for Plain Text (Double-Entry) Accounting with [`beancount`](https://beancount.github.io/) and [`fava`](https://beancount.github.io/fava/) (for the data visualization) to make my personal finances more transparent and convenient to me;
    + An uptime monitor using [Uptime Kuma](https://github.com/louislam/uptime-kuma);
    + An instance of [n8n.io](https://n8n.io/), which is a Zapier/IFTTT alternative, as my automation platform for various things (like gathering data periodically);
    + A [PostgreSQL](https://postgresql.org/) database for my Quantified Self data; and
    + [howis.jskherman.com](https://howis.jskherman.com/) for my personal statistics dashboard because I was inspired by [howisFelix.today?](https://howisfelix.today/) and [this Reddit post](https://www.reddit.com/r/dataisbeautiful/comments/101hvnv/oc_i_tracked_every_hour_of_my_life_for_5_years/).
+ `2023-07-26` During June 2023, while I did have some time to rest for a month, I did some progress towards my pending side projects that I wanted to do after school.
  + I shipped a bare-bones reimplentation of my dashboard site for my Quantified Self statistics at [howis.jskherman.com](https://howis.jskherman.com). It currently only has my Time Tracking data and temperature data that I have been collecting since February 2023 in my PostgreSQL database. I am still working on implementing the data visualizations of the other data I have collected. This is a work in progress and postponed for now because of my board exam preparations.

### January

+ `2023-01-16` Classes are starting again and this time this is the 2nd semester of my fourth year in college for my Bachelor's degree in Chemical Engineering. Judging from the [2018-2019 curriculum](https://buchemengg.wixsite.com/buchedept/downloads), this semester is going to be hectic with classes need to be virtually done by the end of April 2023.

## The Year 2022

### December

+ `2022-12-28` Doing some improvements to my `streamlit` app for personal statistics/dashboard (something like the idea behind [Exist.io](https://exist.io/) but I get to build it myself from scratch).
  + Have made progress creating a page of buttons and small forms to quickly log data for various things I am tracking.
  + Have also made progress in learning how to use DigitalOcean's serverless functions to scrape and save data from the web to a MongoDB database on a regular schedule.

### November

+ `2022-11-28` Doing some improvements to my `streamlit` app for personal statistics/dashboard (something like the idea behind [Exist.io](https://exist.io/) but I get to build it myself from scratch). Have made progress integrating my [Todoist](https://todoist.com) tasks, [Telegram](https://telegram.org/), and [Notion](https://www.notion.so/).

+ `2022-11-15` I am reading Ryan Holiday's book "[Ego is the Enemy](https://g.co/kgs/dv44rZ)". So far after glancing at the table of contents and the first few pages, it seems it would be an interesting read.

+ `2022-11-05` I am reading through the **Mushoku Tensei** Light Novel Series. I am now at [volume 19](https://g.co/kgs/SS4fm1) of the official English-translated light novels.

### August

+ `2022-08-15` The start of the 1st semester of academic year 2022–2023, and the 1st semester of my 4th year studying Chemical Engineering. It seems like things are ramping up and everyone seems eager for the face-to-face hybrid classes.

### July

+ `2022-07-08` I participated as a semi-finalist in the [SCG Bangkok Business Challenge @ Sasin 2022](https://bbc.sasin.edu/2022) at Bangkok, Thailand. I also presented at the [60-second pitch round (01:35:35)](https://www.facebook.com/bangkokbusinesschallenge/videos/435526435096048) for the Opening Reception.

+ `2022-07-29` I joined the National Nutrional Council's first ever Nutri-Hackathon in a team of four and [won first place](https://www.facebook.com/photo.php?fbid=426822102808547) with them.

## The Year 2021

### June

+ `2021-06-21`: Learned the ins and outs of being a Vice President for Internal Affairs in my university's student organization for the Chemical Engineering department: [Philippine Institute of Chemical Engineering - Junior Chapter V (PIChE-JCV)](https://www.facebook.com/PIChEJCV/).

+ `2021-06-26`: Developed this website and the another site for my notes. I have learned a lot about the [Zettelkasten method](https://zettelkasten.de/) and the world of [static site generators](https://jamstack.org/generators/) on the side, little by little, throughout last year.
