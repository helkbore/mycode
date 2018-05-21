#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'5_2读取数据库mysql 2017年11月15日'

__author__ = 'Gentiana'

import pymysql.cursors

# 获取数据库连接
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    db = 'wikiurl',
    charset = 'utf8mb4'

)

try:
    # 获取会话指针
    with connection.cursor() as cursor:
        sql = "select `urlname`, `urlhref` from `urls` where `id` is not null"

        count = cursor.execute(sql)
        # print(count)

        # 查询数据
        # result = cursor.fetchall()
        # print(result)

        result = cursor.fetchmany(size = 3)
        print(result)
finally:
    connection.close()