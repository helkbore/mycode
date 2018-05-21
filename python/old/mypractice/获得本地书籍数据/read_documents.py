#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'读取文件夹内的文件'

import os
import math
import do_db
# print(os.path.abspath("."))
book_dir = "E:\\book\\"

#
# print('begin')
# print(book_dir)
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print('----root')
        # print(root)
        #
        # # list，包含了当前dirpath路径下所有的子目录名字（不包含目录路径）；
        # print('----dirs')
        # print(dirs)
        #
        # # list，包含了当前dirpath路径下所有的非目录子文件的名字（不包含目录路径）
        # print('----files')
        # print(files)

        # 遍历books里面的图书, 获取文件名
        for file in files:
            # print(file)
            print(os.path.splitext(file))


# file_name(book_dir)
files = os.listdir(book_dir)
for file in files:
    book = {}
    # print(file)
    book['file_name'] = os.path.splitext(file)[0]
    book['name'] = book['file_name'].split('-')[0]
    book['author'] = book['file_name'].split('-')[1] if len(book['file_name'].split('-'))  > 1 else '未知'
    book['size'] = os.path.getsize(os.path.join(book_dir, file))
    # book['size'] = math.ceil(os.path.getsize(os.path.join(book_dir, file)) / 1024)
    book['type'] = os.path.splitext(file)[1]
    print(book)
    save_book(book)
