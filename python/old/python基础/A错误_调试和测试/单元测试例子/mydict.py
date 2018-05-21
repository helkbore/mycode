#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'错误,调试和测试-单元测试-例子 2017年11月8日'

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
