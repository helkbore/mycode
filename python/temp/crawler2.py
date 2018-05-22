import myfunc
import db_mysql2
from bs4 import BeautifulSoup

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
