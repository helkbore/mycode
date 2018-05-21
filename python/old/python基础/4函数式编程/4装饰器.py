#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 函数式编程-装饰器 2017年11月6日


'''
@unique装饰器可以帮助我们检查保证没有重复值
'''

# 通过变量调用该函数。
def now():
    print('2017年11月6日')

f = now
f()

print(now.__name__)
print(f.__name__)

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
'''
本质上，decorator就是一个返回函数的高阶函数。
'''

def log(func):
    def wrapper(*args, **kw):
        print('call %s(): ' %func.__name__)
        return func(*args, **kw)
    return wrapper

print('----decorator')


# 装饰器使用
'''把@log放在now定义前, 相当于执行了: now = log(now)'''
@log
def now():
    print('2017年11月6日')

now()

# 定义了参数的装饰器
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s(): " %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

'''相当于 now = log('execute')(now)'''
print('----decorator')
@log('execute')
def now():
    print('2017年11月6日')

now()


print('----decorator')
print(now.__name__)
'''经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper' '''

# 完整的装饰器-不带参数的
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s() :' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 完整的装饰器-带参数的
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

'''
在面向对象（OOP）的设计模式中，decorator被称为装饰模式
'''


# 练习
'''
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

再思考一下能否写出一个@log的decorator，使它既支持：
'''
import functools

def log(text = ''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' %(text, func.__name__))
            func(*args, **kw)
            print('end call')
            return None
        return wrapper
    return decorator

print('----practice')
@log()
def now():
    print('2017年11月6日')

now()