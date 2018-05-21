#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象高级-使用枚举类 2017年11月7日'

# 定义常量
'''
为枚举类型定义一个class类型，
每个常量都是class的一个唯一实例。
Python提供了Enum类来实现这个功能
'''

from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# Enum 派生自定义类

from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

'''@unique装饰器可以帮助我们检查保证没有重复值'''



# 访问枚举类型
print('----访问枚举类型')
day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)