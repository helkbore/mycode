import myfunc
import db_mysql2
from bs4 import BeautifulSoup

urlsets = [
    "http://www.jikezhi.net/navs"
]

prefixs = []

findTag = [
    ['div', 'item'],
    ['h2', ''],
    ['a', '']

]
# urlsets = [
#     "http://www.c3z.cn/Index/hot.html",
#     "http://www.c3z.cn/Index/web.html",
#     "http://www.c3z.cn/Index/object.html",
#     "http://www.c3z.cn/Index/operation.html",
#     "http://www.c3z.cn/Index/design.html",
#     "http://www.c3z.cn/Index/study.html"
# ]
#
# prefixs = [
#     "推荐",
#     "web",
#     "编程",
#     "运维",
#     "设计",
#     "学习"
# ]

# findTag = [
#     ["div", "portlet cardarea"],
#     ["div", "caption"],["span", ""],
#
#     ["a","list-card-details list-card-items popovers"],
#     ["span", "cardinfoa"]
# ]



def do_crawler(urlsets, prefixs, findTag):
    html = []
    result = []
    for url in urlsets:
        html.append(myfunc.get_html(url))

    print("已抓取所有html, 共: " + str(len(html)) + "项")



    for indexHtml in range(len(html)):
        soup = BeautifulSoup(html[indexHtml], 'lxml')
        layer1 = soup.findAll(findTag[0][0],  attrs={'class': findTag[0][1]})

        # print(layer1)
        # exit()

        print(findTag[1][1])
        for l1 in layer1:
            title = l1.find(findTag[1][0], attrs={'class': findTag[1][1]}).text.strip() #.find(findTag[2][0], attrs={'class': findTag[2][1]}).text.strip()

            # print(title)
            # exit()

            layer2 = l1.findAll(findTag[2][0],  attrs={'class': findTag[2][1]})

            # print()
            # print(prefixs[indexHtml])
            for l2 in layer2:
                item = {}
                item['name'] = l2.text # .find(findTag[4][0], attrs={'class': findTag[4][1]}).text.strip()
                item['link'] = l2['href'].strip()
                item['root'] = myfunc.get_root(item['link'])

                # item['tag'] = prefixs[indexHtml]
                item['tag'] = title

                print(item)
                result.append(item)

    print("***********************")
    print("开始插入数据库")
    print("处理项共计: " + str(len(result)))
    db_mysql2.save_item2(result)




do_crawler(urlsets, prefixs, findTag)