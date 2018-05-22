import myfunc
import db_mysql2
from bs4 import BeautifulSoup

url = "http://hao.xsldh.com/"


html = myfunc.get_html(url)
soup = BeautifulSoup(html, 'lxml')

result = []

title_sets = soup.findAll("h2")
# ts2 = soup.findAll("h2", attrs={'class': 'c2'})
# ts3 = soup.findAll("h2", attrs={'class': 'c2'})
# ts4 = soup.findAll("h2", attrs={'class': 'c2'})
# ts5 = soup.findAll("h2", attrs={'class': 'c2'})
# ts6 = soup.findAll("h2", attrs={'class': 'c2'})
# ts7 = soup.findAll("h2", attrs={'class': 'c2'})
# ts8 = soup.findAll("h2", attrs={'class': 'c2'})
# ts9 = soup.findAll("h2", attrs={'class': 'c2'})

title_lists = []

for i in range(len(title_sets)):
    title_lists.append(title_sets[i].text.strip())

print(title_lists)

tab = soup.findAll("ul", attrs={'class': 'pure-g'})

print(len(tab))

for i in range(len(tab)):
    tag = title_lists[i]
    # tag = prefix
    print(tag)

    favs = tab[i].findAll("a", attrs={'class': 'item'})
    for f in favs:
        item = {}
        item['tag'] = tag
        item['name'] = f.text
        item['link'] = f['href']
        item['root'] = myfunc.get_root(f['href'])

        result.append(item)

        print(item)


db_mysql2.save_item2(result)