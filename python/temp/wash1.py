import myfunc
import db_mysql3
from bs4 import BeautifulSoup
import bs4
import requests
import re
import json

# WASH ITEM
itemList = db_mysql3.getAllItem()
# print(len(itemList))
# print(itemList[0])


siteList = []
articleList = []

idTopple2 = []
for i in itemList:
    print(i)
    html1 = myfunc.get_html(i['link'])
    html2 = myfunc.get_html(i['root'])

    # html1 = myfunc.get_html("http://www.baidu.com")
    # html2 = myfunc.get_html("http://www.baidu.com")

    if html1 == html2:
        siteList.append(i)
        idTopple2.append(i['id'])
        print(idTopple2)
    else:
        articleList.append(i)

print("站点共计: " + str(len(siteList)))
print("文章共计: " + str(len(articleList)))

print()
print()
idTopple = []
for i in siteList:
    print(i)
    idTopple.append(i['id'])

db_mysql3.updateItemsSite(idTopple)

