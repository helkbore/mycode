#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'爬取 2017年12月4日'
import requests
from bs4 import BeautifulSoup
import random
import book_db
import time
import os
from datetime import datetime



# -- 公共方法
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "

# -- 爬取集思会
# ---- 爬取集思会书籍分类



def get_jsh_type():
    url = "http://www.kindlepush.com/category"

    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    bl_ul = soup.find("ul", attrs={'class': 'w-list'})
    liTags = bl_ul.find_all('a')
    # print(liTags)

    for l in liTags:
        type = {}
        type['name'] = l.text.strip()[1:-1]
        type['href'] = l["href"]
        print(type)
        book_db.save_type('jsh_type', type)

# ---- 爬取集思会书籍分类
# get_jsh_type()

# -- 抓取豆瓣
# ---- 抓取豆瓣标签分类
def get_db_type():
    url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"

    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    table = soup.findAll("table", attrs={'class': 'tagCol'})
    for t in table:

        title = {}
        tag = {}
        title_a = t.previous_sibling.previous_sibling
        title["label"] = title_a.text.strip()[0:2]
        title["father"] = 0
        insert_id = book_db.save_label("db_label", title)

        tag["father"] = insert_id
        trsorts = t.findAll("tr")
        for tr in trsorts:
            for td in tr.findAll("td"):
                tag["label"] = td.find("a").text.strip()
                book_db.save_label("db_label", tag)
                # print(td.find("a").text)
            # print(tr)
        # print(t)
        time.sleep(10)

        # print(insert_id)
# get_db_type()
# ----抓取豆瓣分类页图书
def get_db_books():
    type="言情耽美"
    base_url = "http://www.kindlepush.com/category/28/0/"
    size = 22
    begin = 1
    for n in range(begin, size + 1):
        # time.sleep(10)
        print("第: " + str(n) + "  页")
        url = base_url + str(n)
        print(url)

        html = get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find("ul", attrs={'class': 'j-list'})
        li = ul.findAll("li", attrs={'class': 'u-bookitm1 j-bookitm'})
        for l in li:
            # time.sleep(5)
            book = {}
            info = l.find("div", attrs={'class': 'info'})
            a = info.find("a", attrs={'class': 'title'})
            book["name"] = a.text.strip().replace("'", "\'\'").replace("/", "_").lstrip('"')
            # print(book["name"])
            book["href"] = a["href"]
            book['cover_link'] = l.img['src']
            book["pingfen"] = info.find("span", attrs={'class': 'num'}).text.strip()[1:-1]
            book["author"] = info.find("div", attrs={'class': 'u-author'}).span.text.strip().lstrip('"').replace('"', "\'\'")
            book["type"] = type

            # 下载图片

            try:
                path = 'E:/downbooks/covers/' + type + "/"
                if (os.path.exists(path) != True):
                    os.mkdir(path)
                if (book['cover_link']):
                    with open(path + book["name"] + '.jpg', 'wb+') as f:
                        f.write(requests.get(book['cover_link']).content)
            except Exception as e:
                continue


            print("【" + str(datetime.now())[0:-6] + "】-" + book["name"] + '-------------' + book["author"] )
            book_db.save_jsh_book("jsh_book", book)
        book_db.logger.info("读取 " + type + "目录下书籍成功")

        # time.sleep(5)

def get_hao123():
    url = "https://www.hao123.com/?tn=91713162_hao_pg"
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    a = soup.findAll("a")
    for l in a:
        # type = {}
        # type['name'] = l.text.strip()
        # type['href'] = l["href"]
        #
        # print(type['name'] + type['href'])
        print(l)

    # print(a)
    # print(html)
# get_hao123()

def get_yishimei():
    base_url = "http://www.yishimei.cn/catalog.asp?page="
    for  n in range(1, 46):
        # print(n)
        url = base_url + str(n)
        print(url)
    pass

get_yishimei()
# get_db_books()