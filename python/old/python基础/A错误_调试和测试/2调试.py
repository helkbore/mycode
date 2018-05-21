#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'错误,调试和测试-调试 2017年11月8日'

# 用print 将可能有问题的变量打印出来

# 断言
'''
凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

如果断言失败，assert语句本身就会抛出AssertionError：
'''

'启动python解释器时可以利用 -0参数来关闭断言'
''' python -0 err.py '''

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d ' %n)
print(10 / n)

'''
logging 的错误级别: debug, info, warning, error

logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
'''


# pdb
'启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。'

'''
输入命令l来查看代码
输入命令n可以单步执行代码
任何时候都可以输入命令p 变量名来查看变量
输入命令q结束调试，退出程序
'''

# pdb 设置断点 pdb.set_trace()
'''
我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
'''

'''
命令p查看变量
命令c继续运行
'''

