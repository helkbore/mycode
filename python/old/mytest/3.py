#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'map()'

def add100(x):
    return x + 100

hh = [11, 22, 33]
print(map(add100, hh))

for i in map(add100, hh):
    print(i)