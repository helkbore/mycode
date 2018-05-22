import re
from urllib.parse import urlparse
import db_mysql

source_path = u"1.txt"

f = open(source_path, encoding="utf-8")
text = f.read()

# print(text)


# 去除多余换行
text = re.sub(r'\n\n', '', text)
text = re.sub(r'\n\s\(', ' (', text)

# 找出括号及其中的网址
list_link = []
p1 = re.compile(r'\(\s+\S+\s+\)')
list_link  = p1.findall(text)

# 找出如 "74) yandex (" 的
p2 = re.compile(r'\d{1,2}\)'+ r'.*?' +r'\(')
t2 = p2.findall(text)



title = []
for t in t2:
    # 去掉数字和括号
    t = re.sub(r'\d{1,2}\)', "", t)
    t = re.sub(r'\(', "", t)
    title.append(t.strip())

result = []
for i in range(len(title)):
    item = {}

    title[i] = re.sub(r'\d{1,2}\)', "", title[i])
    title[i] = re.sub(r'\(', "", title[i])

    list_link[i] = re.sub(r'\(', '', list_link[i])
    list_link[i] = re.sub(r'\)', '', list_link[i])
    item['name'] = title[i].strip()
    item['link'] = list_link[i].strip()

    item['root'] = urlparse(item['link'])[0] + "://" + urlparse(item['link'])[1]


    print(item)
    db_mysql.save_item(item)
    result.append(item)



