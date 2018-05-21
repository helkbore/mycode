#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象高级-元类 2017年11月7日'

'''
Tips:

'''

'函数和类的定义是运行时动态创建的'

# 通过type() 创建新的类型
def fn(self, name = 'world'):
    print('Hello, %s' %name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

'''
type()函数依次传入3个参数：
1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''

'''
通过type()函数创建的类和直接写class是完全一样的，
因为Python解释器遇到class定义时，
仅仅是扫描一下class定义的语法，
然后调用type()函数创建出class。
'''

# metaclass 元类
'先定义metaclass，就可以创建类，最后创建实例'

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda  self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

'''
__new__()方法接收到的参数依次是：

1. 当前准备创建的类的对象；
2. 类的名字；
3. 类继承的父类集合；
4. 类的方法集合。
'''
class MyList(list, metaclass=ListMetaclass):
    pass

'''
例子解释: 
它指示Python解释器在创建MyList时，
要通过ListMetaclass.__new__()来创建，
在此，我们可以修改类的定义，
比如，加上新的方法，然后，返回修改后的定义。
'''

print('---- 元类')
L = MyList()
print(L.add(1))
print(L)