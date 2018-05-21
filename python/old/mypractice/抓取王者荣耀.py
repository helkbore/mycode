#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习-抓取王者荣耀-英雄,金币等 2017年11月10日'

__author__ = 'Gentiana'

import requests
from bs4 import BeautifulSoup

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

# 测试
url = 'http://bang.qq.com/app/yxzj/herov2/index?gameId=20001&uin=877480433&roleName=睡不醒的幼莃&uniqueRoleId=489777735&userId=351708803&token=8BwDFFdk&openid=127B905935C2CD2099838D4BD49B349C&serverName=手Q87区&toOpenid=127B905935C2CD2099838D4BD49B349C&roleId=1044302764&serverId=1097&areaId=1'
url = 'http://bang.qq.com/app/yxzj/herov2/index?gameId=20001&uin=877480433&uniqueRoleId=489777735&userId=351708803&token=8BwDFFdk&openid=127B905935C2CD2099838D4BD49B349C&toOpenid=127B905935C2CD2099838D4BD49B349C&roleId=1044302764&'
url = \
'http://bang.qq.com/app/yxzj/herov2/index?'\
'gameId=20001&'\
'uin=877480433&'\
'roleName=睡不醒的幼莃&'\
'uniqueRoleId=489777735&'\
'userId=351708803&'\
'token=8BwDFFdk&'\
'openid=127B905935C2CD2099838D4BD49B349C&'\
'serverName=&'\
'toOpenid=127B905935C2CD2099838D4BD49B349C&'\
'roleId=1044302764&'\
'serverId=1097&'\
'areaId=1&'\

url = 'http://bang.qq.com/app/yxzj/herov2/index?gameId=20001&roleName=%E6%9C%88%E6%B3%A0%E6%A0%96%E6%A2%A7%E9%98%99&uniqueRoleId=1592482405&nickname=%E6%8C%BD%E6%9C%88%E6%A5%BC%E6%A8%BD&userId=490702454&token=ZjgrS9cK&wxAppid=wxf4b1e8a3e9aaf978&accessToken=q4ubA2nyr_Z4eYs5L2l9UstF87Jyk6pSwyGu67SsPAQRcuWw0iVJk0g1Ow7yMtzsJ5vhRYO2Be3LRZ-ZSKGuFcotnxnvs7i_8KxToaShl14&openid=owanlsgzIPPmrhVUJ8619p_94C7w&serverName=%E5%BE%AE%E4%BF%A178%E5%8C%BA&toOpenid=owanlsgzIPPmrhVUJ8619p_94C7w&appOpenid=oFhrws6-FcJeUlQOCOkxb6-QQPIg&roleId=1232744323&serverId=3088&areaId=3&roleJob=%E5%80%94%E5%BC%BA%E9%9D%92%E9%93%9CIII&isMainRole=1&areaName=%E5%AE%89%E5%8D%93&roleLevel=8&'

# print(url)
html = get_html(url)

soup = BeautifulSoup(html, 'lxml')
# print(print(soup.prettify()))
ul_money = soup.find("ul", attrs={'class': 'mtui-hero-money'})
# print(ul_money)
liTags = ul_money.find_all('span', attrs={'class' : 'num'})
# print(liTags)
money = liTags[0].text.strip()
diamond = liTags[1].text.strip()
# print(money)
# print(diamond)



hero_num = soup.find("ul", attrs={'class': 'mtui-hero-bar'}).find('span', attrs={'class' : 'num'}).text.strip()
# print(hero_num)


own_hero = soup.find_all("ul", attrs={'class' : 'mtui-hero-bd herolist '})
# print(own_hero.__len__())

all_hero_detail = soup.find(id='ownedlist').find_all("ul")
# print(all_hero_detail.__len__())
# print(all_hero_detail)
# print(all_hero_detail[0])
# 所有英雄信息
all_heros = []

def get_hero_detail(heroLists):
    hero_details = []
    for hero in heroLists:
        li = hero.li
        # print(hero.li.img['data-lazysrc'])
        info = {}
        info['hero_id'] = hero['heroid']
        info['type'] = hero['herotype']
        info['name'] = hero.li.p.text.strip()
        info['changci'] = hero.find("li", attrs={"class" : "changci"}).text.strip()


        info['img'] = hero.li.img['data-lazysrc']

        # 下载图片
        #
        # with open('E:/wzry_pic/' + info['name'] + '.png', 'wb+') as f:
        #     f.write(requests.get("http:" + info['img']).content)



        hero_details.append(info)
    return hero_details

# 所有英雄的list
all_heros = get_hero_detail(all_hero_detail)

# 拥有英雄的list
own_heros = get_hero_detail(own_hero)

for h in own_heros:
    print(h['name'], ' : ', h['changci'])
