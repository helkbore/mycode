#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'常用內建模块-datetime 2017年11月21日'
from datetime import datetime, timezone, timedelta

# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# datetime转换为timestamp
print('----时间戳')
print(dt.timestamp() )

'Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数'

'''
某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，
这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
'''

# timestamp转换为datetime
print('------timestamp转换为datetime')
t = 1429417200.0
print(datetime.fromtimestamp(t))

'按当前操作系统设定的时区进行转换'

# str转换位datetime
print('------str转换位datetime')
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

'''
转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
'''
'转换后的datetime是没有时区信息的。'

# datetime转换为str
print('------datetime转换为str')
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
print('------datetime加减')
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

# 本地时间转换为UTC时间
print('------本地时间转换为UTC时间')
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

'''如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。'''

# 时区转换
print('------ 时区转换')

# 拿到UTC时间，并强制设置时区为UTC+0:00:
print(datetime.utcnow())
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))


'''
datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
'''