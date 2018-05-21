def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(list(r))

from functools import reduce
def add(x, y):
    return x + y

reduce(add, [1, 3, 5, 7, 9])


'''
------------------------------------------练习
利用map()函数，把用户输入的不规范的英文名字，
变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
capitalize()
'''

from functools import reduce

def normalize(s):
    return s.capitalize();

L = ['adam', 'LISA', 'barT']
M = list(map(normalize, L))
print(M)

'''
Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用reduce()求积
'''
def prod(L):
    return reduce(lambda x, y: x * y, L)

print(prod([2, 4, 2]))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''
print('----------------------------')
s = '178003.1415926525'

def str2float(s):
    # 小数点分割
    spt = s.split('.')
    print(spt)

    # 转成数字
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    # map和reduce 套用函数
    result = reduce(lambda x, y: 10 * x + y, map(char2num, spt[0])) + 0.1 * reduce(lambda x, y: 0.1 * x + y, map(char2num, spt[1][::-1]))
    return result
print('result : ', str2float(s))