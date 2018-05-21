#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 高级特性-列表生成式 2017年10月31日

# List Comprehensions

# 用来创建list的生成式

# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = [x * x for x in range(1, 11)]
print(L)
'''
写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
'''

# 带if的生成式
L = [x * x for x in range(1, 11) if x %2 == 0]
print(L)

# 两层循环
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 列出当前目录下的所有文件和目录名
import os
L = [d for d in os.listdir('.')]
''' L = [d for d in os.listdir('../')] '''
print(L)

# 使用两个变量
d = {'x' : 'A', 'y' : 'B', 'z' : 'C'}
L = [k + '=' + v for k, v in d.items()]
print(L)

# 将list中所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
nl = [s.lower() for s in L]
print(nl)