#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象编程-继承和多态 2017年11月6日'

__author__ = 'Gentiana'

# 多态
''' 子类定义了一个和父类相同名字的方法(覆盖) '''

# 多态应用

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())

# 扩展: 传入对象不一定是animal类型
'''
对于Python这样的动态语言来说，则不一定需要传入Animal类型。
我们只需要保证传入的对象有一个run()方法就可以了
'''