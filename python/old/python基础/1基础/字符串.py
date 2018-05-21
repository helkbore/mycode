# -*- coding: utf-8 -*-


# 字符串操作 2017年12月7日
import string

'''
去除空格及特殊符号：strip, lstrip, rstrip
复制字符串：str1 = str2
连接字符串
str2 += str1
new_str = str2 + str1
查找字符串：pos = str1.index(str2)
比较字符串：> == <
字符串长度：len(str)
空字符串: 和False等价, 不等于None
'''
# 去除空格
s = '    abcd efg '
s.strip()
s.lstrip()
s.rstrip()

# 字符串连接
print('abc_' + 'defg')
s = 'abcdefg'
s += '\nhijk'
print(str)

# 大写小
s = 'abc defg'
s.upper()
s.upper().lower()
s.capitalize()

# 位置和比较
s_1 = 'abcdefg'
s_2 = 'abdefgh'
print(s_1.index('bcd'))
try:
    print(s_1.index('bce'))
except ValueError:
    print('ValueError: substring not found')

print(s_1 == s_1)  # cmp函数被Python3移除了
print(s_1 > s_2)
print(s_2 > s_1)

# 长度
len(s)

# 分割和连接
s = 'abc,def,ghi'
s.split(',')  # 返回值类型为list
s = '123\n456\n789'
numbers = s.splitlines()  # 按行分割
print('-'.join(numbers))

# 数字到字符串
str(5)

# 格式化字符串
print('Hello %s!' % 'world')
print('%d-%.2f-%s' % (4, -2.3, 'hello'))

print("----格式化字符串")
s = 'abcdefg'
try:
    s[0] = 'x'
except Exception as e:
    print(e)

# 修改字符串
li = list(s)
# print(li)
li[0] = 'x'
s = ''.join(li)
print(s)
s = '-'.join(li)
print(s)

# 切割
s = 'abc,def,ghi'
p1, p2, p3 = s.split(',')
print(p1, p2, p3)

# 下标访问和切片
s = 'abcdefg'
print(s[0], s[-1])
print(s[2:5])
