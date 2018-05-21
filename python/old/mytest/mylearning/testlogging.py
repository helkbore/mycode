#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'学习logging 2017年12月7日'

import logging



# logging.warning("Watch out!") # 打印到控制台

# logging.info("I told you so") # 不会打印任何


# 运行下面的代码必须注释掉上面的warning
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

# 每次日志 不保留之前的记录
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)