+++
title = "get_HN_favorites.py"
description = "A Python script to get HN favorites for a user."
date = 2020-07-15
updated = 2024-03-11
draft = false

[taxonomies]
tags = ["python", "scripting", "csv", "data extraction"]

[extra]
# social_media_card = ""
+++

A Python script to get the Hacker News favorites for a user.

> See original [source](https://github.com/gabrielsroka/gabrielsroka.github.io/blob/c5975c2e4fdc6155bea26a6dcea93287f58ec244/getHNFavorites.py) and [license](https://github.com/gabrielsroka/gabrielsroka.github.io/blob/c5975c2e4fdc6155bea26a6dcea93287f58ec244/LICENSE).

```python
#!/usr/bin/env python3

# Author: gabrielsroka
# Source: https://github.com/gabrielsroka/gabrielsroka.github.io/blob/master/getHNFavorites.py
# License: MIT License

import requests
import time
from bs4 import BeautifulSoup # pip install beautifulsoup4

username = input('username: ')

# session uses connection pooling, often resulting in faster execution.
session = requests.Session()

base = 'https://news.ycombinator.com/'
path = f'favorites?id={username}'
while path:
    r = session.get(base + path)
    s = BeautifulSoup(r.text, 'html.parser')
    for a in s.select('span.titleline a'):
        print(a.text, a['href'])
    more = s.select_one('a.morelink')
    path = more['href'] if more else None
    if path: time.sleep(0.850)
```
