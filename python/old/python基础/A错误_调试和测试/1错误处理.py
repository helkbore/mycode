#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'错误,调试和测试-错误处理 2017年11月8日'

# 错误处理机制
'''
当我们认为某些代码可能会出错时，
就可以用try来运行这段代码，
如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误
如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
'''

'''所有的错误类型都继承自BaseException'''

'''使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽'''

'''
使用try...except捕获错误还有一个巨大的好处，
就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，
这时，只要main()捕获到了，就可以处理
'''

# 调用堆栈

'''
如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
'''

'''堆栈类似于程序出错时的错误跟踪信息'''

# 记录错误 python 内置的logging模块
'''同样是出错，但程序打印完错误信息后会继续执行，并正常退出'''
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('----END')


# 抛出错误
'''
如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
'''


class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' %s)
    return 10 / n

foo('0')

'''
只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型
'''

'''raise语句如果不带参数，就会把当前错误原样抛出。'''
'''捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理'''
'''在except中raise一个Error，还可以把一种类型的错误转化成另一种类型'''