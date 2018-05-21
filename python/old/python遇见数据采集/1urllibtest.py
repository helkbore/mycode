#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'urllib 练习 2017年11月6日'

__author__ = 'Gentiana'

from urllib import request


'''
req = request.Request('')
req.add_header()
req.add_header('User-Agent', '')
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))
'''

req = request.Request('http://www.baidu.com')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))


