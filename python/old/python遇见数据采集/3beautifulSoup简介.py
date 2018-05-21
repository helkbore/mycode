#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用urllib发送post请求 2017年11月6日'

__author__ = 'Gentiana'

from bs4 import BeautifulSoup as bs
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs(html_doc, "html.parser")

# print(soup.prettify())

# print(soup.title)
# print(soup.title.string)
# print(soup.a)
# print(soup.find(id="link2"))
' string 显示的是文本的内容如果有子标签显示none, get_text 可以获取到子标签'
# print(soup.find(id="link2").string)
# print(soup.find(id="link2").get_text())
# print(soup.find_all('a'))
#
# for link in soup.findAll('a'):
#     print(link.string)

print(soup.find("p", {"class" : "story"}))