#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'知乎-从零开始写爬虫-笔记-1.5获取百度贴吧内容 2017年11月7日'

__author__ = 'Gentiana'

'''
网址: http://tieba.baidu.com/f?ie=utf-8&kw=%E7%94%B5%E5%AD%90%E4%B9%A6&fr=search
python: 3.6
lxml, BeautifulSoup

目标:
1. 从网上爬下特定页码的网页
2. 对于爬下的页面内容进行简单的筛选分析
3. 找到每一篇帖子的 标题、发帖人、日期、楼层、以及跳转链接
4. 将结果保存到文本。
'''

import requests
from bs4 import BeautifulSoup

# 抓取网页
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


# 分析网页, 整理信息
def get_content(url):
    comments = []

    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})

    for li in liTags:
        comment = {}
        try:
            comment['title'] = li.find(
                'a', attrs={}).text.strip()
            # print(comment['title'])
            comment['link'] = "http://tieba.baidu.com/" + \
                li.find('a', attrs={'class': 'j_th_tit '})['href']
            comment['name'] = li.find(
                'span', attrs={'class': 'tb_icon_author '}).text.strip()
            comment['time'] = li.find(
                'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find(
                'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            # print(comment)
            comments.append(comment)
            # print(comment)
        except BaseException as e:
            print('出了点小问题', e)
    return comments


def Out2File(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中。

    '''
    with open('TTBT.txt', 'a+', encoding='utf-8') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))

            print('当前页面爬取完成')


def main(base_url, deep):
    url_list = []
    # 将所有需要爬去的url存入列表
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('所有的网页已经下载到本地！ 开始筛选信息。。。。')

    #循环写入所有的数据
    for url in url_list:
        content = get_content(url)
        Out2File(content)
    print('所有的信息都已经保存完毕！')

base_url  = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&fr=search'
deep = 5

# print(get_content(url))

if __name__ == '__main__':
    main(base_url, deep)