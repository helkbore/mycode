#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'正则表达式 2017年11月20日'

# re模块
import re

# 判断匹配
re.match(r'\d{3}\-\d{3,8}$', '010-12345')
print(re.match(r'\d{3}\-\d{3,8}$', '010-12345'))

'''
match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
'''

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

# 切分字符串
print(re.split(r'\s+', 'a b    c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

# 分组
'''
用()表示的就是要提取的分组（Group）
注意到group(0)永远是原始字符串，
group(1)、group(2)……表示第1、2、……个子串
'''
print('----分组')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))


t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

# 贪婪匹配
'''
正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
'''
print('----贪婪匹配')
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 编译
'''
当我们在Python中使用正则表达式时，re模块内部会干两件事情：

编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

用编译后的正则表达式去匹配字符串。
'''

# ==> 预编译
'''
如果一个正则表达式要重复使用几千次，
出于效率的考虑，我们可以预编译该正则表达式，
接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''
import re

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()
re_telephone.match('010-8086').groups()