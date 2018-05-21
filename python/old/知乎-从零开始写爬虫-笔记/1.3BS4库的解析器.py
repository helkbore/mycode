#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'知乎-从零开始写爬虫-笔记-1.3BS4库的解析器 2017年11月6日'

__author__ = 'Gentiana'

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

import bs4
soup = bs4.BeautifulSoup(open('demo.html'), 'lxml')
# print(soup.prettify())

# 手动设置编码方式
# soup = BeautifulSoup(markup, from_encoding="编码方式")

'''
bs4 库将复杂的html文档转化为一个复杂的树形结构，每个节点都是Python对象 ，
所有对象可以分为以下四个类型：Tag , NavigableString , BeautifulSoup , Comment

1. Tag： 和html中的Tag基本没有区别，可以简单上手使用
2. NavigableString： 被包裹在tag内的字符串
3. BeautifulSoup： 表示一个文档的全部内容，大部分的时候可以吧他看做一个tag对象，支持遍历文档树和搜索文档树方法。
4. Comment：这是一个特殊的NavigableSting对象，在出现在html文档中时，会以特殊的格式输出，比如注释类型。
'''

'''tag的.contents属性可以将tag的子节点以列表的方式输出'''
''' 试着输出一下内容...懒得打print了'''
'''
soup.head
soup.title
soup.body.b

tag = soup.find_all('a')
need = tag[1]

head_tag = soup.head
head_tag.contents
title_tag = head_tag.contents[0]
'''

'''另外通过tag的 .children生成器，可以对tag的子节点进行循环：'''
head_tag = soup.head
title_tag = head_tag.contents[1]
# print(title_tag.contents)

# 遍历子节点
for child in title_tag.children:
    print(child)

# 遍历子孙节点
for child in title_tag.children:
    print(child)