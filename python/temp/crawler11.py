import myfunc
import db_mysql2
from bs4 import BeautifulSoup
import bs4
import requests

url = "http://www.its368.com/"
html = myfunc.get_html(url)

soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())


# 左边部分
lpart = soup.find(id="cates")
# print(lpart)

tab = lpart.findAll("div", class_="sub cate-sub")

for t in tab:
    first_title = t.find("div", class_="title").text.strip()
    first_title = first_title.replace("&", "-")
    print(first_title)

    linksSets = t.findAll("a", attrs={'fd': 'style, href, label'})
    # print(len(linksSets))

    for ls in linksSets:
        second_title = {}
        second_title['name'] = ls.text.strip()
        second_title['link'] = "http://www.its368.com" + ls['href']
        # print(second_title)

        print("------开始爬取: " + second_title['link'])
        result = []
        cHtml = myfunc.get_html(second_title['link'])
        cSoup = BeautifulSoup(cHtml, 'html.parser')

        cContent = cSoup.find(id="Shipin_Boke")
        cTab = cContent.findAll("div", class_="sub")
        for ct in cTab:
            third_title = ct.find("div", class_="title").text.strip()
            print(third_title)

            cLinksSets = ct.findAll("a", attrs={'fd': 'style, href, label'})

            for i in cLinksSets:
                item = {}

                item['tag'] = third_title
                # item['tag'] = second_title['name']
                # item['tag'] = first_title

                item['name'] = i.text.strip()
                item['link'] = i['href']
                item['root'] = myfunc.get_root(item['link'])

                result.append(item)
                print(item)

        print("***********************")
        print("开始插入数据库")
        print("处理项共计: " + str(len(result)))
        db_mysql2.save_item2(result)
        result = []


'''
# 更多详情页
content = soup.find(id="cools")
tab = content.findAll("div", class_="sub")
for t in tab:
    first_title = t.find("a", attrs={"name" : "title", "fd" : "href, label"}).text.strip()
    first_title = first_title.replace("[", "")
    first_title = first_title.replace("]", "")
    print(first_title)
    page_link = "http://www.its368.com/" + t.find("a", attrs={"name" : "title", "fd" : "href, label"})['href']

    print("------开始爬取: " + page_link)
    result = []
    cHtml = myfunc.get_html(page_link)
    cSoup = BeautifulSoup(cHtml, "html.parser")
    cContent = cSoup.find(id="Shipin_Boke")
    cTab = cContent.findAll("div", class_="sub")
    for ct in cTab:
        third_title = ct.find("div", class_="title").text.strip()
        print(third_title)

        cLinksSets = ct.findAll("a", attrs={'fd': 'style, href, label'})

        for i in cLinksSets:
            item = {}

            # item['tag'] = third_title
            # item['tag'] = second_title['name']
            item['tag'] = first_title

            item['name'] = i.text.strip()
            item['link'] = i['href']
            item['root'] = myfunc.get_root(item['link'])

            result.append(item)
            print(item)

    print("***********************")
    print("开始插入数据库")
    print("处理项共计: " + str(len(result)))
    db_mysql2.save_item2(result)
    result = []

'''


