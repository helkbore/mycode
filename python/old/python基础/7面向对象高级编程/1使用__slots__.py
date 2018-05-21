#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象高级-使用__slots__ 2017年11月7日'

# 为实例绑定方法
class Student(object):
    pass

def set_age(self, age):
    self.age = age


from types import MethodType
s = Student()
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 为class绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)
s2 = Student()
s2.set_score(99)
print(s2.score)


# __slots__
'限制该class实例能添加的属性'
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.age = 18
print(s.age)
s.score = 99
print(s.score)

# 注意
'''
__slots__定义的属性仅对当前类实例起作用，
对继承的子类是不起作用的
'''


# 注意
'''
在子类中也定义__slots__，
这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
'''