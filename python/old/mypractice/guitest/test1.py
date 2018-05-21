# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore

''' test1 '''
#
# #定义一个窗口程序
# app = QtWidgets.QApplication(sys.argv)
#
# #定义一个窗口对象，用户可以通过接口来自定义
# widget = QtWidgets.QWidget()
#
# widget.resize(360, 360)
# widget.setWindowTitle("Hello, PyQt5!")
# widget.show()
# sys.exit(app.exec_())

'''test2'''

app = QtWidgets.QApplication(sys.argv)

# 用户界面的基本控件
w = QtWidgets.QWidget()

# 窗口大小
w.resize(250, 150)

# 移动到坐标(300, 300)位置
w.move(300, 300)

w.setWindowTitle("Sample-汉字成吗")

# 内存中创建, 显示器上显示
w.show()

sys.exit(app.exec_())