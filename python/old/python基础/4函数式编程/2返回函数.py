#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 函数式编程-返回函数 2017年11月6日

'''函数作为结果值返回'''

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

''' 内部函数可以引用外部函数的参数和局部变量'''
'''
!!!注意，
当我们调用lazy_sum()时，
每次调用都会返回一个新的函数，
即使传入相同的参数
'''
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)
'''f1()和f2()的调用结果互不影响。'''


print('----')
print(list(range(1, 4)))
# 闭包
'''
返回闭包时牢记的一点就是：
返回函数不要引用任何循环变量，
或者后续会发生变化的变量。
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return(i * i)
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())


def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


'''返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。'''