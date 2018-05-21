#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用urllib发送post请求 2017年11月6日'

__author__ = 'Gentiana'

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

'''
req = Request("")
postData = parse.urlencode([])
req.add_header()
resp = urlopen()

print(resp.read().decode('utf-8'))
'''
req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")
postData = parse.urlencode([
    ("StartStation", "fbd828d8-b1da-4b06-a3bd-680cdca4d2cd"),
    ("EndStation", "5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f"),
    ("SearchDate", "2017/11/09"),
    ("SearchTime", "14:00"),
    ("SearchWay", "DepartureInMandarin")
])
req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent",
               "Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36")
resp = urlopen(req, data=postData.encode("utf-8"))



print(resp.read().decode('utf-8'))