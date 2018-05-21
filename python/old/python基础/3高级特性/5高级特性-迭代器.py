#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 高级特性-生成器 2017年11月03日

# 可迭代对象
'''
可以直接作用于for循环的数据类型有以下几种
一类是集合数据类型，
    如list、tuple、dict、set、str等
一类是generator，
    包括生成器和带yield的generator function

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
'''

# 用isinstance()判断 Iterable对象：
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 迭代器
'''可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator'''
from collections import Iterator
print('----迭代器')
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()
print('----迭代器转换')
print(isinstance(iter([]), Iterator))