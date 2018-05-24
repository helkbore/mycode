import myfunc
import db_mysql2
from bs4 import BeautifulSoup
import bs4
import requests

url = "http://www.pitcn.com/index.html"

html = myfunc.get_html_gbk(url)
# print(html)
soup = BeautifulSoup(html, 'lxml')
tab = soup.findAll("div", class_="item")
# print(len(tab))

result = []
for t in tab:
    title = t.find("h2").text.strip()
    print(title)

    linkSets = t.findAll("a")
    for l in linkSets:
        item = {}

        item['tag'] = title
        item['name'] = l.text.strip()
        item['link'] = l['href']
        item['root'] = myfunc.get_root(item['link'])

        result.append(item)
        print(item)


db_mysql2.save_item2(result)

