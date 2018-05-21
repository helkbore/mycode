#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 高级特性-切片 2017年10月31日

'''
Tips
用来截取数组的的
L[1 : 10] : 取第1到第10
L[3 : 5] : 取第1到第10
L[3 : 15 : 2] 每隔2个取第3到第15

L[-2 : ] : 从倒数第二个到最后
L[-5: -2] : 从倒数第5到倒数第2
L[:: -1] : 逆序排列
L[:: -2] : 逆序间隔2排列

'''
#取list前n个元素

# 方法1
print(range(6));
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = [];
n = 3;
for i in range(n):
    print(i)
    r.append(L[i])

print(r);


# 方法2
print(L[0:3]);
'''L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3'''

print(L[-2:]);


# 摘抄
L = list(range(100))

# 前10个数，每两个取一个
print(L[0: 10 : 2]);
print(L[: 10 : 2]);

# 所有数，每5个取一个
print(L[::5]);

# L[:] 原样赋值L
print(L[:]);


print('----------------------------------------------');
# 同理操作touple
'''
tuple也是一种list，唯一区别是tuple不可变。
因此，tuple也可以用切片操作，只是操作的结果仍是tuple
'''
print((0, 1, 2, 3, 4, 5)[:3]);


#同理操作字符串
print('ABCDEFGHIJKL'[:3])
print('ABCDEFGHIJKL'[::2])

print('----test')
L = list(range(15))
print('L:', L)
print(L[-2 : ])
print(L[-5: -1])
print(L[:: -1])
print(L[:: -2])

