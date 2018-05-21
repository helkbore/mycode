# !!!参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。



''' ---------------摘要------------------------------
# 默认参数
(a="abc")

# 可变参数(0个或任意个参数-touple)
(*numbers)
# 命名关键字参数(只接收city, job关键字参数 以*或 可变参数隔开)
def person(name, age, *, city, job)
# 关键字参数(0个或任意个参数-dict)
(**key)


 ---------------摘要------------------------------'''













# 默认参数

# 默认参数的陷阱
def add_end(L=[]):
    L.append('END')
    return L

print(add_end());
print(add_end());
print(add_end());

# 应改为:
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end());
print(add_end());
print(add_end());


# 可变参数
'''可变参数允许你传入0个或任意个参数, 这些可变参数在函数调用时自动组装为一个tuple'''

'''不用可变参数是这样'''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1, 2, 3]));
print(calc([1, 2, 3, 4]));

'''可变参数的定义方式'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2));
print(calc());

nums = [1, 2, 3];
calc(*nums);


# 关键字参数
'''关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict'''
def person(name, age, **kw):
    print("name: ", name, 'age: ', age, 'other: ', kw);

person("michael", 30);
person('bob', 35, city='Beijing');
person('Adam', 45, gender = 'M', job = 'engineer');

extra = {'city': 'Beijing', 'job': 'Engineer'};
person('Jack', 24, **extra);
print('--------------------------------------------------');

#命名关键字参数
'''只接收city和job作为关键字参数
和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
eg: def person(name, age, *args, city, job):
'''
def person(name, age, *, city, job):
    print(name, age, city, job)

print(person('Jack', 24, city='Beijing', job='Engineer'));
