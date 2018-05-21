#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象编程-获取对象信息 2017年11月6日'

__author__ = 'Gentiana'


# type()

class Animal(object):

    def run(self):
        print('Animal is running...')


class Dog(object):

    def run(self):
        print('Animal is running...')


class Husky(object):

    def run(self):
        print('Animal is running...')


a = Animal()
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(a))


# 用type() 判断基本类型
print('----')
print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))


# 用type()判断函数, 对象类型
import types
def fn():
    pass

print('----')
print(type(fn) == types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)


# isinstance()
'''判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。'''
print('----')
a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Dog) and isinstance(d, Animal))
print(isinstance(d, Husky))


# isinstance() 判断基本类型
print('----')
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

# isinstance() 判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# dir()
'''
获取一个对象的所有属性和方法
返回一个list
'''
print('----')
print(dir('ABC'))

# len()方法
'''
len()方法 : 在len()函数内部，它自动去调用该对象的__len__()方法
'''


'''我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法'''
print('----')
print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))


# getattr()、setattr()以及hasattr()
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('----')
# 有属性'x'吗？
print(hasattr(obj, 'x'))
print(obj.x)
# 有属性'y'吗？
print(hasattr(obj, 'y'))
# 设置一个属性'y'
print(setattr(obj, 'y', 19))
print( hasattr(obj, 'y'))
# 获取属性'y'
print(obj.y)

# 如果试图获取不存在的属性，会抛出AttributeError的错误

#print('----不存在属性')
# print( getattr(obj, 'z'))
# 获取属性'z'，如果不存在，返回默认值404
# print(getattr(obj, 'z', 404))



# getattr()、setattr()以及hasattr() 获得对象的方法
print('----获得对象的方法')
# 有属性'power'吗？
print(hasattr(obj, 'power'))
# 获取属性'power'
print(getattr(obj, 'power'))
# 获取属性'power'并赋值到变量fn
fn = getattr(obj, 'power')
# fn指向obj.power
print(fn)
# 调用fn()与调用obj.power()是一样的
print(fn())