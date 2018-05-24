import myfunc
import db_mysql2
from bs4 import BeautifulSoup
import bs4
import requests
import json

url = "http://www.h-ui.net/data/site.json"

r = requests.get(url)
rjson = r.json()
result = []

for i in rjson['data']:
    title = i['name']

    print(title)
    for m in i['data']:
        item = {}
        item['tag'] = title
        item['name'] = m['site']
        item['link'] = m['url']
        item['root'] = myfunc.get_root(item['link'])

        result.append(item)
        print(item)

db_mysql2.save_item2(result)
