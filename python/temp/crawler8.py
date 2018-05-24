import myfunc
import db_mysql2
from bs4 import BeautifulSoup
import bs4

url = "https://navisec.it/"
html = myfunc.get_html(url)
soup = BeautifulSoup(html, 'lxml')

first_title = "纳威安全导航"

'''
#left part
lpart = soup.find("div", class_="l-widget-area entry-content")
second_title = "常用工具"

result = []
for i in lpart.contents:
    # print(type(i))
    if type(i) == bs4.element.NavigableString:
        if len(i.strip()) == 0:
            continue

    # print(type(i))

    if type(i) == bs4.element.Tag:
        # print(i.name)
        if i.name == "h3":
            title = i.text
            print(title)

        if i.name == "a":
            item = {}
            item['tag'] = title
            item['tag'] = second_title
            # item['tag'] = first_title

            item['name'] = i.text.strip()
            item['link'] = i['href']
            item['root'] = myfunc.get_root(item['link'])


            result.append(item)
            print(item)

    if type(i) == bs4.element.Comment:
        print("-----注释 ----")
        # print(str(i))
        commentSoup = BeautifulSoup(str(i), 'lxml')
        # print(commentSoup)
        commentSoupLinks = commentSoup.findAll("a")
        for cl in commentSoupLinks:
            item = {}
            item['tag'] = title
            item['tag'] = second_title
            item['tag'] = first_title

            item['name'] = cl.text.strip()
            item['link'] = cl['href']
            item['root'] = myfunc.get_root(item['link'])

            result.append(item)
        print("-----注释 -e---")

db_mysql2.save_item2(result)



'''

#right part
rpart = soup.find(id="content")
result = []
for i in rpart.contents:
    if type(i) == bs4.element.NavigableString:
        if len(i.strip()) == 0:
            continue

    if type(i) == bs4.element.Tag:
        if i.name == "h2":
            title = i.text.strip()
            print(title)

        if i.name == "table":
            linkSets = i.findAll("a")
            for a in linkSets:
                item = {}
                item['tag'] = title
                # item['tag'] = first_title

                item['name'] = a.text.strip()
                item['link'] = a['href']
                item['root'] = myfunc.get_root(item['link'])

                result.append(item)
                print(item)

        if type(i) == bs4.element.Comment:
            print("-----注释 ----")
            print(i)

db_mysql2.save_item2(result)