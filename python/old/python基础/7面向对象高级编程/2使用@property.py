#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象高级-使用__slots__ 2017年11月7日'

# @property
'Python内置的@property装饰器就是负责把一个方法变成属性调用的'
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

'''
@property的实现比较复杂，我们先考察如何使用。
把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值，
于是，我们就拥有一个可控的属性操作：
'''


# 定义只读属性
'只定义getter方法，不定义setter方法就是一个只读属性'



# 练习
'''
请利用@property给一个Screen对象加上width和height属性，
以及一个只读属性resolution：
'''

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution