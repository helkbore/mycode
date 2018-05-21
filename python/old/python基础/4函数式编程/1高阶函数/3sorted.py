#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 函数式编程-高阶函数-sorted 2017年11月1日

# 排序 对list进行排序
L = sorted([36, 5, -12, 9, -21])
print(L)


# 接收函数, 自定义排序
'''
key指定的函数将作用于list的每一个元素上，
并根据key函数返回的结果进行排序
'''
L = sorted([36, 5, -12, 9, -21], key=abs)
print(L)

# 字符串排序
L = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(L)

# 字符串排序-忽略大小写
L = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(L)

# 字符串排序-反向排序
L = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse=True)
print(L)

# 练习
'''
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)


'''再按成绩从高到低排序：'''
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score, reverse=True)
print(L2)