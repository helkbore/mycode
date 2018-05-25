import myfunc
import db_mysql4
from bs4 import BeautifulSoup

result = []
url = "http://www.jikedaohang.com/"

html = myfunc.get_html(url)
soup = BeautifulSoup(html, "html.parser")
menu = soup.find("ul", class_="layui-nav am-nav am-nav-pills am-topbar-nav am-topbar-right admin-header-list tpl-header-list")
menuItem = menu.findAll("a")
# print(len(menuItem))
# result = []
for i in range(len(menuItem) - 1):
    first_title = menuItem[i].text.strip()
    pageLink = "http://www.jikedaohang.com/" + menuItem[i]['href']

    # print(first_title)
    # print(pageLink)
    cHtml = myfunc.get_html(pageLink)
    cSoup = BeautifulSoup(cHtml, "html.parser")
    main = cSoup.find("div", class_="site-content")

    tab = main.findAll("div", class_="layui-tab layui-tab-card")
    # print(len(tab))


    for m in tab:
        title = m.find("ul").find("li", class_="layui-tab-li").text.strip()
        # print(title)
        # print(len(title))
        favTab = m.find("div", class_="layui-tab-content")
        fav = favTab.findAll("a", class_="box-item")
        for n in fav:
            item = {}
            item['tag'] = []
            item['tag'].append(title)
            item['tag'].append(first_title)
            item['name'] = n.text.strip()

            # item['link'] = ""
            item['link'] = n['href']
            item['fromurl'] = url

            result.append(item)
            # print(item)

print("***********************")
print("开始插入数据库")
print("处理项共计: " + str(len(result)))
db_mysql4.saveResult(result)
# db_mysql4.saveResult_test(result)
result = []



'''
# url = "http://www.jikedaohang.com/index/index/part/id/10/name/IOS.html"
# prefix = "IOS"

# url = "http://www.jikedaohang.com/index/index/part/id/11/name/%E5%89%8D%E7%AB%AF.html"
# prefix = "前端"

# url = "http://www.jikedaohang.com/index/index/part/id/14/name/%E5%90%8E%E7%AB%AF.html"
# prefix = "后端"



# url = "http://www.jikedaohang.com/index/index/part/id/12/name/%E8%AE%BE%E8%AE%A1.html"
# prefix = "设计"

url = "http://www.jikedaohang.com/index/index/part/id/13/name/%E9%9D%A2%E8%AF%95.html"
prefix = "面试"

url = "http://www.jikedaohang.com/index/index/part/id/15/name/%E6%96%87%E7%AB%A0.html"
prefix = "文章"

html = myfunc.get_html(url)
soup = BeautifulSoup(html, 'lxml')

result = []

tab = soup.findAll("div", attrs={'class': 'layui-tab layui-tab-card'})
# print(tab)

for t in tab:
    item = {}
    # tag = t.find("li",  attrs={'class': 'layui-tab-li'}).text.strip()
    tag = prefix


    favs = t.findAll("a", attrs={'class': 'box-item'})
    for f in favs:
        # print(f)
        item = {}
        item['tag'] = tag
        item['name'] = f.text
        item['link'] = f['href']
        item['root'] = myfunc.get_root(f['href'])

        result.append(item)

        print(item)

        # print(item)

# for i in result:
#     print(i)

db_mysql2.save_item2(result)
'''
