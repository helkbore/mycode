#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习-抓取王者荣耀-英雄,金币等 2017年11月10日'

__author__ = 'Gentiana'

import requests
from bs4 import BeautifulSoup
import random

# 从一系列的user-agent里随机挑出一个符合标准的使用
def get_agent():
    '''
    模拟header的user-agent字段，
    返回一个随机的user-agent字典类型的键值对
    '''
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    fakeheader = {}
    fakeheader['User-agent'] = agents[random.randint(0, len(agents))]
    return fakeheader

    # 注意看新的请求函数：

    def get_html(url):
        try:
            r = requests.get(url, timeout=30, headers=get_agent())
            r.raise_for_status
            r.encoding = r.apparent_encoding
            return r.status_code
        except:
            return "Someting Wrong！"