import myfunc
import db_mysql4
from bs4 import BeautifulSoup


url = "https://shouku123.com/xizi"
# url = "https://shouku123.com/xizi/%E5%85%B6%E4%BB%96"
html = myfunc.get_html(url)
soup = BeautifulSoup(html, 'html.parser')


tab = soup.findAll("li", class_="urlGroupItem")
result = []
for t in tab:
    title = t.find("ul", class_="list-group collapse in urls ")['title']
    print(title)

    linkList = t.findAll("a")
    for i in linkList:
        item = {}
        item['tag'] = []
        item['tag'].append(title)
        item['name'] = i.text.strip()

        lUrl = "https://shouku123.com/" +i['href']
        # item['link'] = ""
        item['link'] = myfunc.get_location(lUrl)

        item['fromurl'] = url

        result.append(item)
        print(item)

print("***********************")
print("开始插入数据库")
print("处理项共计: " + str(len(result)))
db_mysql4.saveResult(result)
'''
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
url = "https://shouku123.com/xizi/%E5%85%B6%E4%BB%96"
html = get_html(url)
soup = BeautifulSoup(html, 'lxml')

liSets = soup.findAll("li", attrs={'class': 'urlGroupItem'})

items = []

for li in liSets:
    title = ""
    ulTitle = li.find("ul",  attrs={'class': 'list-group collapse in urls '})
    # print(ulTitle)
    # exit()
    title = ulTitle['title']

    linkLis = li.findAll("li",  attrs={'class': 'list-group-item'})
    for linkLi in linkLis:
        link = {}
        link['tag'] = title
        lUrl = "https://shouku123.com/" + linkLi.a['href']

        link['link'] = get_location(lUrl)
        link['name'] = linkLi.a.text


        link['root'] = urlparse(link['link'])[0] + "://" + urlparse(link['link'])[1]
        db_mysql.save_item(link)
        # print(link['root'])

        print(link)
    print(title)

# print(html)
'''