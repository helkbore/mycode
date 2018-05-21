#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### tuple 2017年10月30日

'''
tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
'''

# tuple陷阱
t = (1, 2)  # 正常的tuple
t = ()      # 空的tuple
t = (1)     # 问题来了, 这个不是tuple, 这个是小括号~
t = (1, )   # 消除歧义, 这个是tuple
'''
Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
'''


# 可变的tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
t

'''
tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
'''


''' ##############################################################课后练习
'''
# list 和 tuple 的课后练习
# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]


# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

print('-------------------------------');
# 补充
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值，
t = (1, 2, 3);
x, y, z = t;
print(x)
print(y)
print(z)
