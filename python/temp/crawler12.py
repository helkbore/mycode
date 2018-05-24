import myfunc
import db_mysql2
from bs4 import BeautifulSoup
import bs4
import requests
import re
import json

json_url = "http://lackar.com/aa/open_link.js"

r = requests.get(json_url)
rjson = r.text
rjson = "{" + re.sub(r'.*?{', "", rjson, 1)
index = rjson.find("}\n\nfunction")
rjson = rjson[:index + 1]
njson = eval(rjson)
njson['kugou'] = {}
njson['kugou']['home'] = "http://www.kugou.com/"

# print(njson)
# exit()


url = "http://lackar.com/aa/"
html = myfunc.get_html(url)
soup = BeautifulSoup(html, "html.parser")


main = soup.find("div", class_="entrances")

tab = soup.findAll("div", class_="catalog")

result = []
for t in range(len(tab) - 1):
    title = tab[t].find("p", class_="catalogname").text.strip()

    showLinkSets = tab[t].findAll("div", class_=re.compile(r'top|sub'))
    print(len(showLinkSets))
    for i in showLinkSets:
        # print(i.p.text)
        item = {}

        item['tag'] = title
        item['name'] = i.p.text.strip()
        if njson.__contains__(i.img['id']):
            item['link'] = njson[i.img['id']]['home']
            item['root'] = myfunc.get_root(item['link'])
        else:
            item['link'] = ""
            item['root'] = ""

        result.append(item)
        print(item)

db_mysql2.save_item2(result)
