#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'6_2python读取pdf文档 2017年11月15日'
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams

__author__ = 'Gentiana'

'pdfminer3k'

'''
安装pdfminer3k
官网下载, 解压
cmd 进入路径输入
cd E:\pythonCode\pdfminer3k-1.3.1
python setup.py install
'''



# 获取文档对象
fp = open("naacl06-shinyama.pdf", "rb")

# 创建一个与文档关联的分析器
parser = PDFParser(fp)

# PDF文档的对象
doc = PDFDocument()

# 连接分析器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 初始化文档
doc.initialize("")

# 创建PDF资源管理器
resource = PDFResourceManager()

# 参数分析器
laparam = LAParams()

# 创建一个聚合器
device = PDFPageAggregator(resource, laparams=laparam)

# 创建解释器
interpreter = PDFPageInterpreter(resource, device)

# 使用文档对象得到页面的集合
for page in doc.get_pages():
    # 使用页面解释器来读取
    interpreter.process_page(page)

    # 使用聚合器来获得内容
    layout = device.get_result()

    for out in layout:
        if hasattr(out, "get_text"):
            print(out.get_text())
