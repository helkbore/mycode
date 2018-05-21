#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2017年12月8日'

'''
1、请用python编写函数find_string，从文本中搜索并打印内容，要求支持通配符星号和问号。
例子：
 >>>find_string('hello\nworld\n','wor')
['wor']
>>>find_string('hello\nworld\n','l*d')
['ld']
>>>find_string('hello\nworld\n','o.')
['or']

'''

import re
def find_string(str, pat):
    # return re.findall(pat, str, re.I)
    return re.findall(pat, str, re.I)
'''
re.I    表示不区分大小写
re.A    仅匹配ascii
re.L    locale dependent
re.M    多行
re.S    不匹配所有
re.X    冗长的
'''
print(find_string('hello\nworld\n','o.'))

