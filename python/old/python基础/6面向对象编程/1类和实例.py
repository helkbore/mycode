#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象编程-类和实例 2017年11月6日'

__author__ = 'Gentiana'


# 类定义
class Student(object):
    pass

'''
(object)，表示该类是从哪个类继承下来的
通常，如果没有合适的继承类，就使用object类
'''


# 实例化
bart = Student()
print(bart)
print(Student)

bart.name = 'Bart Simpson'
print(bart.name)


# __init__
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

'''self就指向创建的实例本身'''

bart = Student('Bart Simpson', 59)
print(bart.name)
print(bart.score)


# 数据封装
def print_score(std):
    print('%s: %s' %(std.name, std.score))
print_score(bart)

'''没必要额外定义函数来访问---类的方法'''

# 类的方法
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

print('-------')
bart = Student('Bart Simpson', 59)
bart.print_score()


