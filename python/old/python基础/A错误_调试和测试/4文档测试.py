#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'错误,调试和测试-单元测试-例子 2017年11月8日'

# 文档注释

'''
代码与其他说明可以写在注释中
由一些工具来自动生成文档
可以自动执行写在注释中的这些代码
Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。
只有测试异常的时候，可以用...表示中间一大段烦人的输出

如果程序有问题, 运行就会报错
'''
def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)

'''
告诉函数的调用者该函数的期望输入和输出。
'''