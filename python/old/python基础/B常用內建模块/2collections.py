#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'常用內建模块-collections 2017年11月22日'

## namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，
并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
'''

'用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。'
print(isinstance(p, Point)) # 验证创建的point对象是tuple的子类
print(isinstance(p, tuple))

## deque
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

'''
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
'''

## defaultdict
'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。

除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

## OrderedDict
'如果要保持Key的顺序，可以用OrderedDict：'
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('c', 3), ('b', 2), ('a', 1)])
print(od)
'''
OrderedDict的Key会按照插入的顺序排列，不是Key本身排'''
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))