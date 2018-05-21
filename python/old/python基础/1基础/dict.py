#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### dict(map) 2017年10月30日



''' ---------------摘要------------------------------'''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

''' ---------------摘要------------------------------'''









'''
dict全称dictionary，在其他语言中也称为map，
使用键-值（key-value）存储，具有极快的查找速度
'''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])


# 要避免key不存在的错误，有两种办法，
# 一是通过in判断key是否存在：
print('Thomas' in d)

# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get("Bob"))         #75
print(d.get("Bob", -1))     #75

print(d.get("Thomas"))      #None
print(d.get("Thomas", -1))  #-1


### !!! 注意：返回None的时候Python的交互式命令行不显示结果。

# dict的key必须是不可变对象。


# 通过key计算位置的算法称为哈希算法（Hash）

# list 类型不能作为key
