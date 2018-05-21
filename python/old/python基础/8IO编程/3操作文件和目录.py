#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'IO-操作文件和目录 2017年11月15日'

import os

# 查看系统类型
print(os.name)

# 查看用户名(windows系统不能用)
# os.uname()

# 环境变量
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.environ.get('x', 'default'))

# 操作文件和目录
# 查看当前目录的绝对路径:
# print(os.path.abspath("."))

# 把两个路径合成 (不能直接拼接路径)
# print(os.path.join('Users/michael', 'testdir'))

# 创建一个目录:
# os.mkdir('testdir')
# 删掉一个目录:
# os.rmdir('/Users/michael/testdir')

# 拆分路径
# os.path.split('/Users/michael/testdir/file.txt')

# 得到文件扩展名
# 'os.path.splitext()可以直接让你得到文件扩展名'
# os.path.splitext('/path/to/file.txt')

# 重命名
# os.rename('test.txt', 'test.py')

# 删除文件
# os.remove('test.py')

# 复制文件
'shutil模块提供了copyfile()的函数'

# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

