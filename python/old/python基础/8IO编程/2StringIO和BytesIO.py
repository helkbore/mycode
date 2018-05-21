#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'IO-StringIO, BytesIO 2017年11月9日'

# StringIO
'在内存中读写'

'''
f.write('str')
f.getvalue()

'''

from io import StringIO
f = StringIO()
print(f.write("Hello"))
print(f.write(" "))
print(f.write("world"))
print(f.getvalue())


from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO
'''BytesIO实现了在内存中读写bytes'''

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())


from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
