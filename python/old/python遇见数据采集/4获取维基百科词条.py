#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'4获取维基百科词条 2017年11月15日'

__author__ = 'Gentiana'

# 引入开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 请求url并把结果用UTF-8编码
resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")

# 使用BeautifulSoup解析
soup = BeautifulSoup(resp, "html.parser")
listUrls = soup.findAll("a", href=re.compile("^/wiki/"))

# 获取所有以/wiki/开头的a标签到href属性
for url in listUrls:
    if  not re.search("\.(jpg|JPG)$", url['href']):
        print(url.get_text(), '<---------->',"https://en.wikipedia.org" + url['href'])
# print(listUrls)