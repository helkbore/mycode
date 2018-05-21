#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### set 2017年10月30日
s = set([1, 2, 3]);
print(s);

'''
{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，
显示的顺序也不表示set是有序的。
重复元素在set中自动被过滤
'''

s = set([1, 1, 2, 2, 3, 3])
print(s);

# add(key)
s.add(4);
print(s);

# remove(key)
s.remove(3);
print(s);

# 区别, 理解
'''
set和dict的唯一区别仅在于没有存储对应的value
set的原理和dict一样，所以，同样不可以放入可变对象
因为无法判断两个可变对象是否相等，
也就无法保证set内部“不会有重复元素
'''
s1 = set([1, 2, 3]);
s2 = set([2, 3, 4]);
print(s1 & s2);
print(s1 | s2);

