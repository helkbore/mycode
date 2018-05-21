#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'数据库操作 2017年12月1日'

import sqlite3

def save_dict(table, d,select_sql):
    conn = sqlite3.connect('E:\\备份\\sqlite\\kindlebook.db')
    cursor = conn.cursor()

    # 先查询后插入(其实可以用sql: insert or ignore)
    cursor.execute(select_sql)
    result = cursor.fetchall()

    # 说明数据库没有该条记录, 可以进行插入
    if len(result) == 0:
        # --构造insert sql语句
        cols = ','.join(d.keys())
        dvalue = list(d.values())

        # ----将list中的其他类型转换为str
        for s in dvalue:
            dindex = dvalue.index(s)
            dvalue[dindex] = str(s).strip()

        values = "','".join(dvalue)
        values = "'" + values + "'"
        values = '","'.join(dvalue)
        values = '"' + values + '"'

        sql = "insert into %s ( %s ) values ( %s )" % (table, cols, values)

        cursor.execute(sql)
        rowid = cursor.lastrowid

        cursor.close()
        conn.commit()
        conn.close()
        return rowid
    else:
        # logger日志设置省略
        # logger.info("导入失败的书: ")
        # logger.info(d)
        pass

