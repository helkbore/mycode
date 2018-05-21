#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'知乎-从零开始写爬虫-笔记-1.1requests库安装与使用 2017年11月6日'

__author__ = 'Gentiana'

'''
pip install requests
pip list
'''

import requests
r = requests.get("http://www.baidu.com")
print(r.text)

'''
params : 字典或字节序列，作为参数增加到url中

data : 字典、字节序列或文件对象，作为Request的内容 json : JSON格式的数据，作为Request的内容

headers : 字典，HTTP定制头

cookies : 字典或CookieJar，Request中的cookie

auth : 元组，支持HTTP认证功能

files : 字典类型，传输文件

timeout : 设定超时时间，秒为单位

proxies : 字典类型，设定访问代理服务器，可以增加登录认证

allow_redirects : True/False，默认为True，重定向开关

stream : True/False，默认为True，获取内容立即下载开关

verify : True/False，默认为True，认证SSL证书开关

cert : 本地SSL证书路径

url: 拟更新页面的url链接

data: 字典、字节序列或文件，Request的内容

json: JSON格式的数据，Request的内容
'''
#
# #HTTP请求的返回状态，比如，200表示成功，404表示失败
# print (r.status_code)
# #HTTP请求中的headers
# print (r.headers)
# #从header中猜测的响应的内容编码方式
# print (r.encoding)
# #从内容中分析的编码方式（慢）
# print (r.apparent_encoding)
# #响应内容的二进制形式
# print (r.content)

# requests抓取网页的通用框架

import requests

def getHtmlTexl(url):
    try:
        r = requests.get(url, timeout=30)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong!"

url = 'http://bang.qq.com/app/yxzj/herov2/index?gameId=20001&uin=877480433&roleName=睡不醒的幼莃&uniqueRoleId=489777735&userId=351708803&token=8BwDFFdk&openid=127B905935C2CD2099838D4BD49B349C&serverName=手Q87区&toOpenid=127B905935C2CD2099838D4BD49B349C&roleId=1044302764&serverId=1097&areaId=1&roleJob=倔强青铜III&isMainRole=0&areaName=安卓&roleLevel=8'
result = getHtmlTexl(url)


# import bs4
# soup = bs4.BeautifulSoup(result, 'lxml')
# print(soup)