import myfunc
import db_mysql2
from bs4 import BeautifulSoup
import bs4
import requests

def get_html(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = 'gbk'
    # html = r.content
    # html_doc = str(html, 'utf-8')
    return r.text

url = "http://daohang.itqiyi.com/"
html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')

part1 = soup.find("div", attrs={'id': 'qiaoqiao_cate'})
# print(part1)

part1_title_sets = part1.findAll("h2")

# 第一种title
part1_title_list = []
for pts in part1_title_sets:
    part1_title_list.append(pts.text.strip())

print("左边部分大类目, 里面的项目要分页摘取")
print(part1_title_list)

part1_ul_sets = part1.findAll("ul")
pageList = []
for pus in part1_ul_sets:
    pages = pus.findAll("a")
    # print(pages)
    for p in pages:
        result = []
        page = {}
        page['name'] = p.text.strip()
        page['link'] = p['href']
        # print(page)
        pageList.append(page)

        # 循环里面的链接爬取每一页
        print("开始爬取子页面 " + page['link'])
        childPage = get_html(page['link'])
        childSoup = BeautifulSoup(childPage, "lxml")
        childTab = childSoup.find("div", attrs={'class': 'qiaoqiao_bd1'})

        childTitleSets = childTab.findAll("h3")

        childTitleLists = []
        for cts in childTitleSets:
            childTitleLists.append(cts.text.strip())

        childUl = childTab.findAll("ul")

        for cu_i in range(len(childUl)):
            childLinks = childUl[cu_i].findAll("a")
            for cl in childLinks:
                item = {}
                item['tag'] = childTitleLists[cu_i]
                # item['tag'] = page['name']
                # item['tag'] = part1_title_list[part1_ul_sets.index(pus)]

                item['name'] = cl.text.strip()
                item['link'] = cl['href']
                item['root'] = myfunc.get_root(item['link'])

                result.append(item)
                print(item)
        print("***********************")
        print("开始插入数据库")
        print("处理项共计: " + str(len(result)))
        db_mysql2.save_item2(result)
        result = []




# print(html)
# part1 = soup.findAll("table")
# for p in part1:
#     p.findAll("div",  attrs={'class': 'qiaoqiao_box'})
#     print(len(p))
#     for pp in p:
#         print(pp)
#
# tableSets = soup.findAll('table')
# print(tableSets)