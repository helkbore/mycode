import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import db_mysql

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'UTF-8'
        return r.text
    except: return "ERROR"

def get_location(url):
    r = requests.get(url, timeout=30, allow_redirects=False)
    # print(r.headers['location'])
    return r.headers['location']

url = "https://shouku123.com/xizi"
html = get_html(url)
soup = BeautifulSoup(html, 'lxml')

liSets = soup.findAll("li", attrs={'class': 'urlGroupItem'})

items = []

for li in liSets:
    title = ""
    ulTitle = li.find("ul",  attrs={'class': 'list-group collapse in urls '})
    title = ulTitle['title']

    linkLis = li.findAll("li",  attrs={'class': 'list-group-item'})
    for linkLi in linkLis:
        link = {}
        link['type'] = title
        lUrl = "https://shouku123.com/" + linkLi.a['href']

        link['link'] = get_location(lUrl)
        link['name'] = linkLi.a.text


        link['root'] = urlparse(link['link'])[0] + "://" + urlparse(link['link'])[1]
        db_mysql.save_item(link)
        # print(link['root'])

        print(link)
    print(title)

# print(html)