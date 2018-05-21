#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象高级-定制类 2017年11月7日'

# __str__
'定制打印(print)这个对象时的格式'
class Student(object):
    def __init__(self, name):
        self.name = name
print(Student('Michael'))

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__
print(Student('Michael'))

# __repr__
'''
在命令行模式下直接敲变量显示的, 是__repr__
__str__()返回用户看到的字符串，
而__repr__()返回程序开发者看到的字符串，
也就是说，__repr__()是为调试服务的
'''


# __iter__
'''
果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，
该方法返回一个迭代对象，
Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

# __getitem__
'list化'
class Fib(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a

print('----getitem')
f = Fib()
print(f[5])

# 实现切片功能
'没有对step 和 负数进行处理'
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
print(f[0:5])


#  __getattr__
'''
调用不存在的属性时该怎么处理
注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None
'''
class Student(object):
    def __init__(self):
        self.name = 'Micheal'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name)
print(s.score)


# __call__
'''
调用实例本身
'''
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Micheal')
s()

# 判断是函数还是对象
''' 即判断是否为函数 或带有 __call__的类实例'''
print('----')
print(callable(Student('Michieal')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))