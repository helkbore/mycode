#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'笔记 2017年11月6日'

__author__ = 'Gentiana'

# urllib
'''
Python 3.x中提供的一系列操作URL的库
'''

# urllib 使用步骤
'''
导入urllib库
    from urllib import request
请求URL
    resp = request.urlopen('http://www.baidu.com')
使用相应对象输出数据
    print(resp.read().decode("utf-8"))
'''

'''
w       以写的方式打开
a       以追加模式打开(从EOF开始, 必要时创建新文件)
r+      以读写模式打开
w+      以读写模式打开
a+      以读写模式打开
rb      以二进制读模式打开
wb      以二进制写模式打开
ab      以二进制追加方式打开
rb+     以二进制读写模式打开
wb+     以二进制读写模式打开
ab+     以二进制读写模式打开
'''