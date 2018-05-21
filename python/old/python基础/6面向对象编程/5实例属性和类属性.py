#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象编程-实例属性和类属性 2017年11月6日'

__author__ = 'Gentiana'


# 类属性
'''归类所有, 但类的所有实例都可以访问到'''

class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)

s.name = 'Micheal'
print(s.name)
print(Student.name)

del s.name
print(s.name)

'''
不要把实例属性和类属性使用相同的名字，
因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，
再使用相同的名称，
访问到的将是类属性。
'''