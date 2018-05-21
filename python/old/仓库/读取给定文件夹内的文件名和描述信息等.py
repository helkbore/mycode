#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'读取文件夹内的文件 2017年12月1日'

import os

from datetime import datetime

#########################################################################################
# --------------涉及到的模块及方法 ----------------------------------------------------------#
# os.path.abspath(".")
#     返回一个标准的绝对路径名 path
#
# os.walk()
#     遍历目录树，自顶向下或自底向上生成目录树下的文件名。
#     对根目录top（包括根目录top本身）中的每个目录，它都会yield一个3元元组(dirpath, dirnames, filenames)。
#         dirpath是一个字符串，为目录路径。
#         dirnames是dirpath中子目录的名称列表（不包括'.'和'..')。
#         filenames 为dirpath 下非目录文件的名称列表。
#
# os.listdir()
#     返回一个list，包含给定path 目录下所有条目的名字。
# --------------------------------------------------------------------------------------#
##########################################################################################
book_dir = "E:\\book\\"
book_dir = "E:\\downbooks\\new"


# ------------ 方法1 --------------
def file_name(file_dir):

    for root, dirs, files in os.walk(file_dir):

        # 遍历books里面的图书, 获取文件名
        for file in files:
            # print(file)
            print(os.path.splitext(file))


# file_name(book_dir)


# ----------- 方法2 ----------------
files = os.listdir(book_dir)
n = 0
for file in files:
    n = n + 1
    book = {}

    book['origin_name'] = os.path.basename(file)
    book['book_name'] = os.path.splitext(file)[0].split('-')[0].strip()
    book['author'] = book['origin_name'].split('-')[1].strip() if len(book['origin_name'].split('-'))  > 1 else '未知'
    book['size'] = os.path.getsize(os.path.join(book_dir, file))
    # book['size'] = math.ceil(os.path.getsize(os.path.join(book_dir, file)) / 1024)
    book['ext'] = os.path.splitext(file)[1][1:]

    print("【" + str(datetime.now())[0:-7] + "】-" + book["book_name"] + '-------------' + book["author"])

print("---end" + "共 " + str(n) + "条")
