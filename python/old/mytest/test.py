#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
想验证一下这句话什么意思
env_overrides = {k[7:]: v for k, v in os.environ.items() if
                     k.startswith('SCRAPY_')}
'''
import os
print(type(os.environ.items()))

for k, v in os.environ.items():
    print("----------------")
    print(k)
    print(v)

env_overrides = {k[7:]: v for k, v in os.environ.items()}

print(env_overrides)

