#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 函数式编程-高阶函数-filter 2017年11月1日
# filter()函数用于过滤序列。

# 删掉偶数, 只保留奇数
''' 传入 filter 的函数 返回值一般为true/false'''
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(L)

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
L = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))


# 素数

# 1. 构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 2. 定义一个筛选器
def _not_divisible(n):
    return lambda x: x % n > 0  # n 为 _not_divisible的传参, x 为 it

# 3. 定义生成器
def primes():
    yield 2
    it = _odd_iter()    #初始序列
    while True:
        n = next(it)    #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构建新序列

for n in primes():
    if n < 5:
        print(n)
    else:
        break

# 练习
'''
回数是指从左向右读和从右向左读都是一样的数，
例如12321，909。
请利用filter()滤掉非回数：
'''
print('----pracitce')
def is_palindrome(n):
   s = str(n)
   return s[:] == s[::-1]


output = filter(is_palindrome, range(1, 1000))
print(list(output))


