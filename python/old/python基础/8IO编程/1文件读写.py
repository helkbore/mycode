#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'IO-文件读写 2017年11月9日'

# 同步异步
'''
CPU和内存书序远高于外设
同步IO: 程序暂停后续代码, 传输完再执行
异步IO: 传输的同时程序继续执行, 不等待IO执行的结果
'''

'''
操作IO的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用
'''

# 读文件
f = open('testio.txt', 'r')
print(f.read())
f.close()

# try ... finnally
'''
由于文件读写时都有可能产生IOError，
一旦出错，后面的f.close()就不会调用。
所以，为了保证无论是否出错都能正确地关闭文件，
我们可以使用try ... finally来实现
'''
try:
    f = open('testio.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# with 自动close
with open('testio.txt', 'r') as f:
    print(f.read())

'''
read(size)最多读取size个字节的内容
readline()可以每次读取一行内容
readlines()一次读取所有内容并按行返回list
'''

# file-like Object
'''
像open()函数返回的这种有个read()方法的对象，
在Python中统称为file-like Object。
除了file外，还可以是内存的字节流，网络流，自定义流等等。
file-like Object不要求从特定类继承，只要写个read()方法就行。

StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
'''

# 二进制文件
'图片视频等二进制文件 用rb 模式打开文件'
f = open('test.jpg', 'rb')
print(f.read())

# 字符编码
'要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数'
f = open('gbktest.txt', encoding='gbk')
print(f.read())

'遇到编码错误直接忽略'
f = open('gbktest.txt', 'r', encoding='gbk', errors='ignore')

# 写文件
f = open('testio.txt', 'w')
f.write('Hello, world~~~~!')
f.close()

with open('testio.txt', 'w') as f:
    f.write('Hello, world````!')

'''
要写入特定编码的文本文件，
请给open()函数传入encoding参数，
将字符串自动转换成指定编码。
'''