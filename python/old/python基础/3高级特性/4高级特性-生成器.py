#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 高级特性-生成器 2017年11月02日

'''
如果列表元素可以按照某种算法推算出来，
那我们是否可以在循环的过程中不断推算出后续的元素呢？
'''

# 一边循环一边计算的机制，称为生成器

# 创建generator
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));
# print(next(g));
'''越界会抛出StopIteration的错误'''

# 用循环输出
for n in g:
    print(n)

# 斐波拉契数列
'''(除第一个和第二个数外，任意一个数都可由前两个数相加得到) '''

    # 函数实现
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print('fib')
print(fib(10))

'''
a, b = b, a + b
相当于
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
'''


    # 生成器实现
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print('生成器实现斐波拉契数列 : ')
f = fib(6)
print(next(f))


'''
用for循环调用generator时，
发现拿不到generator的return语句的返回值。
如果想要拿到返回值，
必须捕获StopIteration错误，
返回值包含在StopIteration的value中
'''

print('捕获错误版: ');
g = fib(6)
while True:
    try:
        x = next(g)
        print('g : ', x)
    except StopIteration as e:
        print('Generator return value: ', e.value)
        break


# yield
'''
函数是顺序执行
    遇到return语句或者最后一行函数语句就返回。
变成generator的函数，
    在每次调用next()的时候执行，
    遇到yield语句返回，
    再次执行时从上次返回的yield语句处继续执行。
'''


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield (5)

print('生成器函数执行顺序: ')
o = odd()
print(next(o))
print(next(o))
print(next(o))


# 练习: 杨辉三角
def tri(num):
    L = [1]
    for n in range(num):
        yield L
        L = [1]+[L[i]+L[i+1] for i in range(n)]+[1]

print('杨辉三角')
for t in tri(10):
    print(t)

