#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'IO-序列化 2017年11月15日'

# 序列化
'把变量从内存中变成可存储或传输的过程称之为序列化'

# pickle.dumps()
'把任意对象序列化成一个bytes'
import pickle
d = dict(name = 'Bob', age = 20, score = 88)
pickle.dumps(d)

# 读取变量并保存本地
f = open("dump.txt", 'wb')
pickle.dump(d, f)
f.close()

# 反序列化
f = open("dump.txt", 'rb')
d = pickle.load(f)
f.close()
print(d)

'''
Pickle的问题和所有其他编程语言特有的序列化问题一样，
就是它只能用于Python，
并且可能不同版本的Python彼此都不兼容，
因此，只能用Pickle保存那些不重要的数据，
不能成功地反序列化也没关系。
'''


# JSON
import json
d = dict(name = 'Bob', age = 20, score = 88)
print(json.dumps(d))

json_str = '{"age" : 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

# JSON进阶 class

import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 类的__dict__属性
'''
通常class的实例都有一个__dict__属性，
它就是一个dict，用来存储实例变量。
也有少数例外，比如定义了__slots__的class
'''

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))