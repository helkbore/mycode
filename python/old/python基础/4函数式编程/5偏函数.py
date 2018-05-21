#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 函数式编程-偏函数 2017年11月6日
import functools
int2 = functools.partial(int, base = 2)
print(int2('1001'))

'''
functools.partial的作用就是，
把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单
'''

# 注意
'''
注意到上面的新的int2函数，
仅仅是把base参数重新设定默认值为2，
但也可以在函数调用时传入其他值
'''

i = int2('9999', base = 10)
print(i)

'''
当函数的参数个数太多，需要简化时，
使用functools.partial可以创建一个新的函数，
这个新函数可以固定住原函数的部分参数，
从而在调用时更简单。
'''