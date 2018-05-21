import re
'''
'r' 时表示只是读取文件；
 w 表示只是写入文件（已经存在的同名文件将被删掉）；
'a' 表示打开文件进行追加；写入到文件中的任何数据将自动添加到末尾。
'r+'表示打开文件进行读取和写入。
'''

f = open(u'D:\\personal\\字幕\\基础代数\\线性方程一.srt', encoding='utf-8')
srt = f.read()

# 去掉时间
p = r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}'
srt = re.sub(p, '', srt)

# 格式化序号前的换行
srt = re.sub(r'\n(\d{1,3})\n\n', r'\n\1\n', srt)

with open(u'D:\personal\字幕\格式化后\基础代数\线性方程一.txt', 'w', encoding='utf-8') as file:
    file.write(srt)

