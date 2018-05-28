import myfunc
import db_mysql2
from bs4 import BeautifulSoup

url = "http://www.gogeeks.cn/nav"


html = myfunc.get_html(url)
soup = BeautifulSoup(html, 'html.parser')

result = []

divTab = soup.find("div", class_="ui grid")
h4LIst = divTab.findAll("h4", class_='ui header')


first_title_list = []
for i in range(1, len(h4LIst)):
    print(h4LIst[i].text.strip())
    first_title_list.append(h4LIst[i].text.strip())
# print((first_title_list))
exit()




'''
pageTab = soup.findAll("div", attrs={'class': 'm-list1 m-list1-c1'})

cats = []
for t in tab:
    catagory = t.findAll("a")
    for c in catagory:
        cat = {}
        cat['name'] = c.text.strip()
        cat['link'] = "http://www.gogeeks.cn" + c['href'].strip()
        cats.append(cat)

        fhtml = myfunc.get_html(cat['link'])
        fsoup = BeautifulSoup(fhtml, 'lxml')
        ftab = fsoup.findAll("a", attrs={'class': 'more'})
        ftag = []
        for ft in ftab:
            tttemptag = ft.text.strip()
            tttemptag = tttemptag.replace("•", "-")
            ftag.append(tttemptag)


        ul_list = fsoup.findAll("ul", attrs={'class': 'f-cb'})


        for ii in range(len(ul_list)):
            ffav = ul_list[ii].findAll("a", attrs={'class': 'link'})
            result = []
            print()
            print(ftag[ii] + "--" + cat['name'])


            for ff in ffav:
                fitem = {}
                fitem['name'] = ff.find("span", attrs={'class': 'tt'}).text.strip()
                fitem['link'] = ff['href'].strip()
                fitem['root'] = myfunc.get_root(fitem['link'])

                fitem['tag'] = ftag[ii]
                # fitem['tag'] = cat['name']
                result.append(fitem)
                print(fitem)

            print("***********************")
            print("开始插入数据库")
            print("处理项共计: " + str(len(result)))
            db_mysql2.save_item2(result)

            print("--------------------------")
            # for r in result:
            #     print(r)
            #
            # result = []
    # print(len(result))









# db_mysql2.save_item2(result)

'''