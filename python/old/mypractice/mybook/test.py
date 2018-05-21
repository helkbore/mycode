import requests
from bs4 import BeautifulSoup
'''
def get_yishimei():
    for x in range(1 ,46):
        print("http://www.yishimei.cn/catalog.asp?page="+ str(x) )
get_yishimei()

def get_html(url):
    r = requests.get(url), timeout=30)
    r.encoding = "utf-8"
    return r.text
'''

def get_yishimei():
    base_url = 'http://www.yishimei.cn/catalog.asp?page='
    for x in range(1, 2):
        url = base_url + str(x)
        print(url)
        html = get_html(url)
        # print(html)

        soup = BeautifulSoup(html , 'lxml')
        # print(soup)
        div = soup.find("div",attrs={'class':'post cate5 auth1'})
        div = soup.find("div",attrs={'class':'post cate5 authl'})
        print(div)
    pass
def get_html(url):
    r = requests.get(url, timeout=30)
    r.encoding = "utf-8"
    # print(r.text)
    return r.text
get_yishimei()

