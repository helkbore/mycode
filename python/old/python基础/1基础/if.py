#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 条件判断 2017年10月30日


''' ---------------摘要------------------------------'''


''' ---------------摘要------------------------------'''













age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
    # else 后面的 冒号 : 不要忽略

'''
if语句执行有个特点，
它是从上往下判断，
如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
'''


# 简写
x = 123;
if x:
    print('True')
    

# 例子
''' 要点
input 输入的是字符串, 要和数字比较需要类型转换
'''
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

''' ##############################################################课后练习
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
'''
height = 1.77
weight = 100.25
result = weight/(height * height)

if result < 18.5:
    print('过轻');
elif result >= 18.5 and result <= 25:
    print('正常');
elif result >= 25 and result <= 28:
    print('过重');
elif result >= 28 and result <= 32:
    print('肥胖');
elif result >32:
    print('严重肥胖');

