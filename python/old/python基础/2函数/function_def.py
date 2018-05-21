#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 函数 2017年10月30日

'''
定义一个函数要使用def语句，
依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，
函数的返回值用return语句返回。
'''

# return
'''
如果没有return语句，函数执行完毕后也会返回结果，
只是结果为None。
return None可以简写为return。
'''

# 定义
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


# 调用
'''
如果你已经把my_abs()的函数定义保存为abstest.py文件了，
那么，可以在该文件的当前目录下启动Python解释器，
用from abstest import my_abs来导入my_abs()函数，
注意abstest是文件名（不含.py扩展名）
'''

# pass 占位符
age = 10
if age >= 18  :
    prss;
    
def nop():
    pass;
'''
如果想定义一个什么事也不做的空函数，可以用pass语句：
pass可以用来作为占位符
'''

# 返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi/6);
print(x, y);

r = move(100, 100, 60, math.pi/6);
print(r);

'''
原来返回值是一个tuple！
但是，在语法上，返回一个tuple可以省略括号，
而多个变量可以同时接收一个tuple，按位置赋给对应的值，
所以，Python的函数返回多值其实就是返回一个tuple，
但写起来更方便。
'''

''' ##############################################################课后练习
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。
'''


import math
print(math.sqrt(4));
def quadratic(a, b, c):
    result_1 = (-b + math.sqrt( b *b - 4 * a * c)) / (2 * a)
    result_2 = (-b - math.sqrt(b*b - 4 * a * c)) / (2 * a)
    return result_1, result_2;
print(quadratic(2, 3, 1))
