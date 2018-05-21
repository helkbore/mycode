#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'数据库操作 2017年12月1日'

import sqlite3
import logging


logop = {}
global logger
logop['logfile'] = "log.txt"
logop['loglevel'] = "INFO"
logger = logging.getLogger()
hdlr = logging.FileHandler(logop['logfile'], encoding="utf-8")
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
try:
  logger.setLevel(logop['loglevel'])
except:
  print("你输入的日志等级不正确")



def save_book(table, d):
    sql = "select id from %s where book_name = '%s' and ext = '%s' and size = %s " % (table, d['book_name'], d['ext'], d['size'])
    save_dict(table, d, sql)

def save_type(table, d):
    sql = "select id from %s where name = '%s'  " % (table, d['name'])
    # print(sql)
    save_dict(table, d, sql)

def save_label(table, d):
    sql = "select id from %s where label = '%s'  " % (table, d['label'])
    # print(sql)
    rowid = save_dict(table, d, sql)
    return rowid

def save_jsh_book(table, d):
    # sql = "select id from %s where name = '%s'  " % (table, d['name'])
    sql = "select id from " + table + " where name = " + '"' +  d['name'] + '"'
    # print(sql)
    rowid = save_dict(table, d, sql)
    return rowid

def save_dict(table, d,select_sql):
    conn = sqlite3.connect('E:\\备份\\sqlite\\kindlebook.db')
    cursor = conn.cursor()

    # -- 构建select 语句
    # sql = "select id from %s where book_name = '%s' and ext = '%s' " % (table, d['book_name'], d['ext'])
    # print(sql)
    cursor.execute(select_sql)
    result = cursor.fetchall()
    # print()
    if len(result) == 0:



        # --构造insert sql语句
        cols = ','.join(d.keys())
        # ----将list中的其他类型转换位str
        dvalue = list(d.values())
        for s in dvalue:
            dindex = dvalue.index(s)
            dvalue[dindex] = str(s).strip()

        values = "','".join(dvalue)
        values = "'" + values + "'"
        values = '","'.join(dvalue)
        values = '"' + values + '"'

        sql = "insert into %s ( %s ) values ( %s )" % (table, cols, values)

        # print(sql)



        cursor.execute(sql)
        rowid = cursor.lastrowid
        # print(rowid)
        # print(cursor.rowcount)
        cursor.close()
        # print("-- book_db.save_book")
        conn.commit()
        conn.close()
        return rowid
    else:
        # print("导入失败的书: ")
        logger.info("导入失败的书: ")
        logger.info(d)
        # print(d)

# d = {'book_name': 'test', 'size': '100', 'ext': 'mobi', 'origin_name': 'test.mobi'}
# table = 'book'
# # save_dict('book', book)
# sql = "select id from %s where book_name = '%s' and ext = '%s' " % (table, d['book_name'], d['ext'])
# print(sql)

# conn = sqlite3.connect('E:\\备份\\sqlite\\kindlebook.db')
# cursor = conn.cursor()
# sql = "select book_name from book"
# cursor.execute(sql)
#
# info = {}
# allBook = []
# for i in cursor.fetchall():
#     info['book_name'] = i[0]
#     allBook.append(info)
# print(allBook)
#
# conn.commit()
# conn.close()
