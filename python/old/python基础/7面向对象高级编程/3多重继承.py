#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象高级-多重继承 2017年11月7日'

# 多重继承
'一个子类就可以同时获得多个父类的所有功能'
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class Bat(Mammal, FlyableMixIn):
    pass

class Dog(Mammal, RunnableMixIn):
    pass


# MixIn
'''
如果需要“混入”额外的功能，通过多重继承就可以实现
这种设计通常称之为MixIn。
'''