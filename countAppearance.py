#!/usr/bin/env python

URLs, urls =[],  ["http://www.google.com/a.txt", "http://www.google.com.tw/a.txt", "http://www.google.com/download/c.jpg", "http://www.google.co.jp/a.txt", "http://www.google.com/b.txt", "https://facebook.com/movie/b.txt", "http://yahoo.com/123/000/c.jpg", "http://gliacloud.com/haha.png", ]

from urllib.parse import urlparse
for s in urls:URLs.append(urlparse(s).path.split('/')[-1])
unique=set(URLs)
for u in unique:print(u, URLs.count(u))
