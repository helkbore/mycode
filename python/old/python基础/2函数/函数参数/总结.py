def func(x, y = 500):
    pass

func(150)
func(100, 200)
func(y = 300, x = 100)

# 可变参数
def func(name, *numbers):
    print(name)
    print(numbers)

func('Tom', 1, 2, 3, 4)

# 关键字参数
def func(name, **kvs):
    print(name)
    print(kvs)

func('Jack', china = 'Beijing', uk = 'London')

# 命名关键字参数
def func(*, china, uk): # *用于和普通参数做分割，*args一样效果
    print(china, uk)

func(china = 'Beijing', uk = 'London')  # 必须传入参数名


# 参数顺序
'必选参数、默认参数、可变参数、命名关键字参数和关键字参数。'