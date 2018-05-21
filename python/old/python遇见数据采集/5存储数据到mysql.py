#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'5存储数据到mysql 2017年11月15日'

__author__ = 'Gentiana'

'pip install pymysql'

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors

'''
# 获取数据库连接
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    db = 'wikiurl',
    charset = 'utf8mb4'

)

# 获取会话指针
connection.cursor()

# 执行SQL语句
cursor.execute(sql, (a, b))

# 提交
connection.commit()

# 关闭
connection.close()
'''

'''
读取mysql数据

# 得到总记录数
cursor.execute()

# 查询下一行
cursor.fetchone()

# 得到指定大小
cursor.fetchmany(size=None)

# 得到全部
cursor.fetchall()
'''

# 请求url并把结果用UTF-8编码
resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")

# 使用BeautifulSoup解析
soup = BeautifulSoup(resp, "html.parser")
listUrls = soup.findAll("a", href=re.compile("^/wiki/"))

# 获取所有以/wiki/开头的a标签到href属性
for url in listUrls:
    if  not re.search("\.(jpg|JPG)$", url['href']):
        print(url.get_text(), '<---------->',"https://en.wikipedia.org" + url['href'])
        # 获取数据库连接
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='wikiurl',
            charset='utf8mb4'
        )

        try:
            # 获取会话指针
            with connection.cursor() as cursor:
                sql = "insert into `urls`(`urlname`, `urlhref`) values(%s, %s)"

                # 执行sql语句
                cursor.execute(sql, (url.get_text(), "https://en.wikipedia.org" + url['href']))

                # 提交
                connection.commit()
        finally:
            connection.close()
