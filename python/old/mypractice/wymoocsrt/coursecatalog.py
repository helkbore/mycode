import requests
from bs4 import BeautifulSoup
import re
import sqlite3

url = 'http://open.163.com/special/Khan/algebra.html'


# -- 公共方法
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'GBK'
        return r.text
    except:
        return " ERROR "

html = get_html(url)
soup = BeautifulSoup(html, 'lxml')
courses_cells = soup.findAll("td", attrs={'class': 'u-ctitle'})
courses = []


conn = sqlite3.connect('E:\\备份\\sqlite\\spiders.db')
cursor = conn.cursor()

for td in courses_cells:
    course = {}
    course['num'] = td.text.strip()
    course['num'] = re.sub(r'(\D+)', '', course['num'])
    # print(td.a.text)
    course['name'] = td.a.text
    # print(course['name'])
    sql = "insert into wygkk_kcml (num, name, course_name) values (" + course['num'] + ",'" + course['name'] + "', '基础代数')";
    conn.execute(sql)
    print(sql)

conn.commit()
conn.close()
