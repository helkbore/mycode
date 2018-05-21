#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
dict(x.split('=', 1) for x in arglist)

'''

# a = {'one': '1+1=2', 'two': '2+2=4', 'three': '3+3=6'}
#
# for x in a:
#     print(x)
# d = dict(x+"!" for x in a)
# print(d)

# a = dict(one=1, two=2, three=3)
# print(a)

l = ["1 + 1 = 2", '2+2=4', '3+3=6']

d1 = [x.split('=', 1) for x in l]
print(d1)

d = dict(x.split('=', 1) for x in l)
print(d)
x = "1 + 1 = 2 = 5 = 6 == 7"
print(x.split('=', 1))
print(x.split('='))