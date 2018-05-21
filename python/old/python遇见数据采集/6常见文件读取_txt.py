#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'6常见文件读取_txt 2017年11月15日'

__author__ = 'Gentiana'

from urllib.request import urlopen
html = urlopen('https://en.wikipedia.org/robots.txt')
print(html.read().decode("utf-8"))