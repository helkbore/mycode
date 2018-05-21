#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 高级特性-迭代 2017年10月31日

# 迭代dict (key)
d = {'a': 1, 'b': 2, 'c': 3};
for key in d:
    print(key);


print("----------------------------------");

# 迭代dict 的 value
for value in d.values():
    print("value : ", value);

print("----------------------------------");

# 迭代dict 的 key 和 value
for key, value in d.items():
    print("key : ", key)
    print("value : ",value)



# 迭代字符串
for ch in 'ABC':
    print(ch)

# 判断是否能够被迭代
from collections import Iterable

print(isinstance('abc', Iterable))

# 经典数组遍历
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)