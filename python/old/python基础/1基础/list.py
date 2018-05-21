#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####### list 2017年10月30日

##############################################

classmates = ['Michael', 'Bob', 'Tracy']
li = [1, 2, 3, 4, 5]
print(classmates);

# list的长度
print(len(classmates));

# 显示单个元素
print(classmates[-1]);
print(classmates[2]);

# 末尾插入
classmates.append('Adam')
print(classmates);

# 插入到指定地方
classmates.insert(1, 'Jack')
print(classmates);

# 删除List末尾
classmates.pop()
print(classmates);
# 删除元素
li.pop()    # => [1, 2, 3, 4]
print(li)
li.pop(2)   # => [1, 2, 4]
print(li)



# 把某个元素替换成别的元素
classmates[1] = 'Sarah'
print(classmates);

# list里面的元素的数据类型也可以不同


# 摘抄
L = list(range(100))


print("--遍历")
li = [1, 2, 3, 4, 5]
# 遍历
for i in li:
    print(i)

# 用range模拟for (i = 0; i < x; ++i)
# range(x) => [0, x - 1]
# range(x, y) => [x, y - 1]
# range(x, y, z) => [x, x + z,..., < y]
for i in range(len(li)):
    # print(li[i])
    pass

for i in range(1, 10, 2):
    print(i)

# 负数索引
print(li[-1])
print(li[-2])

# 负数step的range => [x, x - z, ..., > z]
for i in range(3, -1, -1):
    print(i)



# 按元素添加数组
li = [1, 2]
li_2 = [3, 4, 5]
# 我们想要[1, 2, 3, 4, 5]
# li.append(li_2) => [1, 2, [3, 4, 5]]
li.extend(li_2)
print(li)


li = [5, 8, 7, 4, 2, 3]
li.sort()
print(li)
# lambda帮助排序
li = [[5, 2], [3, 8], [2, 11], [7, 6]]
# li.sort(key = lambda x: x[0]) # 参数名字
# 与lamda等价写法
def item_key(x):
    return x[0]
li.sort(key = item_key)
print(li)