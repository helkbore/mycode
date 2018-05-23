import myfunc
import db_mysql2
from bs4 import BeautifulSoup
import bs4

url = "http://it2048.cn/"


html = myfunc.get_html(url)
soup = BeautifulSoup(html, 'lxml')

# print soup.prettify()



typeLayer1 = soup.find_all("h3", class_="w-tit1")
typeList = []
# print(type(typeLayer1))
# print(isinstance(typeLayer1, BeautifulSoup.element.ResultSet))
commonList = []

result = []

typeDic = {
    "bgmsc" : "bgmusic",
    "bgvdo" : "bgvedio",
    "bgbk" : "bgbook",
    "bgsft" : "bgsoft",
    "bgimga" : "bgimgae"
}

for t in typeLayer1:
    tabList = []
    commonList.append(t.contents[0])
    classType = t.findAll("span")
    for c in classType:
        type = {}
        type['name'] = c.text.strip()
        type['class'] = c['class'][0]
        # print(type)
        tabList.append(type)
    typeList.append(tabList)

# for i in typeList:
#     print(i)


tab = soup.findAll("ul", class_="m-tags")

for i in range(len(tab)):
    tag = commonList[i]
    li = tab[i].findAll("li")

    for l in li:
        a = l.find("a")
        p = l.find("p")
        # print(p['class'][0])
        print()
        print(commonList[i])
        for m in typeList[i]:
            # print(typeDic[m['class']])
            if p['class'][0] == typeDic[m['class']]:
                item = {}
                item['tag'] = m['name']
                # item['tag'] = commonList[i]

                item['name'] = p.text
                item['link'] = a['href']
                item['root'] = myfunc.get_root(item['link'])
                print(item)
                result.append(item)

db_mysql2.save_item2(result)


