import re
import sqlite3

conn = sqlite3.connect('E:\\备份\\sqlite\\spiders.db')
cursor = conn.cursor()
sql = "select num, `name` from wygkk_kcml where course_name = '基础代数'"
cursor.execute(sql)
catalogs = cursor.fetchall()
conn.commit()
conn.close()

source_path = u"D:\\personal\\字幕\\基础代数\\"
source_ext = '.srt'
finnal_path = u"D:\\personal\\字幕\\格式化后\\基础代数\\"
finnal_ext = '.txt'
for items in catalogs:

    s_path = source_path + str(items[1]) + source_ext
    f = open(s_path, encoding='utf-8')
    srt = f.read()

    # 去掉时间
    p = r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}'
    srt = re.sub(p, '', srt)

    # 格式化序号前的换行
    srt = re.sub(r'\n(\d{1,3})\n\n', r'【\1】-', srt)
    # print(srt)
    # exit()
    # m = re.match(r'(1)', srt)
    # print(m.group(0))
    # print(srt.find('\n\n'))
    srt = "【1】-" + srt[srt.find('\n\n') + 2:]
    # srt.replace('1\n\n', '【1】-')
    # srt = re.sub(r'\n(^1\n\n)', r'【1】-', srt)
    srt = srt.replace('\n\n', '\n')
    # print(srt)
    # exit()

    f_path = finnal_path + str(items[0]) + finnal_ext
    catalogs_path = finnal_path + "目录" + finnal_ext
    with open(f_path, 'w', encoding='utf-8') as file:
        file.write(srt)

    catalog_item = "【" + str(items[0]) + "】" + items[1] + '\n'
    with open(catalogs_path, 'a', encoding='utf-8') as file:
        file.write(catalog_item)


    srt = ''
    catalog_item = ''



















