import re
from urllib.parse import urlparse
import db_mysql

path = u"2.txt"


f = open(path, encoding='utf-8')
text = f.read()


# 以---------------------------------------- 切割
text = re.split("----------------------------------------", text)

resu = []
index = 0
for i in text:
    item = {}
    print(index)
    index = index + 1

    i = re.split("\n", i.strip())


    item['type'] = i[0].strip()

    # print(i)

    k = 1
    for k in range(1, len(i)):
        # item['name'] = v
        txt = i[k]
        print(txt)
        title = re.search(r'.*?\s*?\(', txt).group()

        title = re.sub(r':\s*\(', '', title)
        # print(title)
        link = re.search(r'\(.*?\)', txt).group()
        link = re.sub(r'\(|\)', '',link).strip()

        item['name'] = title
        item['link'] = link
        item['root'] = urlparse(item['link'])[0] + "://" + urlparse(item['link'])[1]

        db_mysql.save_item(item)
        print(item)
        # print(txt)

        pass
    # print(item)
    # print(len(i))
    # print(i)