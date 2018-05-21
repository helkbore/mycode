#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### 模块 2017年11月6日

'''任何模块代码的第一个字符串都被视为模块的文档注释；'''


# 作用域
'''
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等

'''


from PIL import Image
im = Image.open('test.jpg')
print(im.format, im.size, im.mode)

im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')


# 模块搜索路径
'''
默认情况下，
Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，
搜索路径存放在sys模块的path变量中
'''
import sys
print(sys.path)

# 手动添加搜索目录
''''
1, 直接修改sys.path
2. 设置环境变量PYTHONPATH
'''
import sys
sys.path.append('/Users/michael/my_py_scripts')