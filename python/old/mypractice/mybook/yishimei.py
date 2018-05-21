import requests
from bs4 import BeautifulSoup

def get_yishimei():
    f_path = u"D:\\亦是美.txt"
    base_url = "http://www.yishimei.cn/catalog.asp?page="
    list = []
    for  n in range(1, 46):
        url = base_url + str(n)

        # 获取html
        html = get_html(url)

        # 解析html文档
        soup = BeautifulSoup(html, 'lxml')
        h4_sets = soup.findAll("h4", attrs={'class': 'post-date'})

        for h4 in h4_sets:
            item = {}

            div = h4.parent
            link = div.find("a")


            item['date'] = h4.text.replace("年", "-").replace("月", "-").replace("日", "")
            item['title'] = link.text
            item['link'] = link['href']

            info = "【" + item['title'] + "】 " + "-------" + item['date'] + "\n" + item['link']
            info = item['date'] + "\t" +  "【" + item['title'] + "】 " +  "\t" + item['link'] + "\n"
            list.append(item)

            with open(f_path, 'a', encoding='utf-8') as file:
                file.write(info)
            print(info)







def get_html(url):
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}
    r = requests.get(url, timeout=30)
    r.encoding = 'utf-8'
    # print(r.text)
    return r.text



# get_html("http://www.yishimei.cn/catalog.asp")
get_yishimei()