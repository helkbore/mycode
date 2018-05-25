import myfunc
import db_mysql4
from bs4 import BeautifulSoup


url = "http://hao.xsldh.com/"
result = []

html = myfunc.get_html(url)
soup = BeautifulSoup(html, "html.parser")


pageSets = soup.findAll("div", class_="swiper-slide")
# print(len(pageSets))
for i in pageSets:
    second_title = []
    first_title = i.find("h1").text.strip()
    # print(first_title)
    titleSets = i.findAll("h2")
    for m in titleSets:
        # print(m.text.strip())
        second_title.append(m.text.strip())



    tabSets = i.findAll("ul", class_="pure-g")

    for m in range(len(tabSets)):
        linkSets = tabSets[m].findAll("a", class_="item")

        for n in linkSets:
            item = {}

            item['tag'] = []
            item['tag'].append(n.text.strip())
            item['tag'].append(second_title[m])
            item['tag'].append(first_title)
            item['name'] = n.text.strip()

            # item['link'] = ""
            item['link'] = n['href']
            item['fromurl'] = url

            result.append(item)

print("***********************")
print("开始插入数据库")
print("处理项共计: " + str(len(result)))
db_mysql4.saveResult(result)
# db_mysql4.saveResult_test(result)
result = []




# url = "http://hao.xsldh.com/"
#
#
# html = myfunc.get_html(url)
# soup = BeautifulSoup(html, 'lxml')
#
# result = []
#
# title_sets = soup.findAll("h2")
#
# title_lists = []
#
# for i in range(len(title_sets)):
#     title_lists.append(title_sets[i].text.strip())
#
# print(title_lists)
#
# tab = soup.findAll("ul", attrs={'class': 'pure-g'})
#
# print(len(tab))
#
# for i in range(len(tab)):
#     tag = title_lists[i]
#     # tag = prefix
#     print(tag)
#
#     favs = tab[i].findAll("a", attrs={'class': 'item'})
#     for f in favs:
#         item = {}
#         item['tag'] = tag
#         item['name'] = f.text
#         item['link'] = f['href']
#         item['root'] = myfunc.get_root(f['href'])
#
#         result.append(item)
#
#         print(item)
#
#
# db_mysql2.save_item2(result)