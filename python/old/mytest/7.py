#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


def getlog(info):
    logger = logging.getLogger()
    hdlr = logging.FileHandler(info['logfile'])
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    try:
        logger.setLevel(info['loglevel'])
    except:
        print
        "你输入的日志等级不正确"
    return logger



logop = {}
logop['logfile'] = "log.txt"#uop['logfile']
logop['loglevel'] = "INFO"#uop['level']
global logger
logger = getlog(logop)#构造log对象

