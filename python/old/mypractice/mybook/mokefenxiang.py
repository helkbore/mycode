import requests
from bs4 import BeautifulSoup
import re

def get_subject(base_url, page, prefix, f_path):
    # f_path = u"D:\\慕课大巴课程列表-AI-20180316.txt"
    # base_url = "https://www.mukedaba.com/forum.php?mod=forumdisplay&fid=87&orderby=dateline&filter=author&orderby=dateline&page="
    list = []
    print(f_path)
    for  n in range(1, page+1):
        url = base_url + str(n)


        # 获取html
        html = get_html(url)


        # 解析html文档
        soup = BeautifulSoup(html, 'lxml')
        table_sets = soup.findAll("a", attrs={'class' : 's xst'})

        for link in table_sets:
            item = {}
            item['title'] = link.text
            item['link'] = prefix + link['href']
            item['title'].encode("utf-8")
            item['link'].encode("utf-8")
            info = "【" + item['title'] + "】 " + "-------" + item['link'] + "\n"
            print(info)
            with open(f_path, 'a', encoding='utf-8') as file:
                file.write(info)

        # h4_sets = soup.findAll("h4", attrs={'class': 'post-date'})
        #
        # for h4 in h4_sets:
        #     item = {}
        #
        #     div = h4.parent
        #     link = div.find("a")
        #
        #
        #     item['date'] = h4.text.replace("年", "-").replace("月", "-").replace("日", "")
        #     item['title'] = link.text
        #     item['link'] = link['href']
        #
        #     info = "【" + item['title'] + "】 " + "-------" + item['date'] + "\n" + item['link']
        #     info = item['date'] + "\t" +  "【" + item['title'] + "】 " +  "\t" + item['link'] + "\n"
        #     list.append(item)
        #
        #     with open(f_path, 'a', encoding='utf-8') as file:
        #         file.write(info)
        #     print(info)







def get_html(url):
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}
    r = requests.get(url, timeout=30)
    # r.encoding = 'utf-8'
    # print(r.text)
    return r.text



# get_html("http://www.yishimei.cn/catalog.asp")
def get_mooc():
    items = []


    item = {}
    # 慕课分享
    infos = []
    info = (49, 1, "人工智能")
    infos.append(info)

    info = (2, 5, "JAVA")
    infos.append(info)

    info = (37, 3, "python")
    infos.append(info)

    info = (38, 2, "PHP")
    infos.append(info)

    info = (39, 1, "前端")
    infos.append(info)

    info = (50, 1, "数据分析")
    infos.append(info)

    info = (62, 1, "web安全")
    infos.append(info)

    for info in infos:
        base_url = "http://www.mkefx.com/forum.php?mod=forumdisplay&fid=" + str(
            info[0]) + "&filter=author&orderby=dateline&page="
        page = info[1]
        prefix = "http://www.mkefx.com/"
        f_path = u"D:\\爬取\\慕课分享课程列表-" + str(info[2]) + "-20180320.txt"

        get_subject(base_url, page, prefix, f_path)


    # 慕课大巴
    infos = []
    info = (87, 3, "人工智能")
    infos.append(info)

    info = (76, 8, "JAVA")
    infos.append(info)

    info = (78, 4, "python")
    infos.append(info)

    info = (79, 4, "PHP")
    infos.append(info)

    info = (80, 8, "前端")
    infos.append(info)

    info = (88, 2, "数据分析")
    infos.append(info)

    info = (104, 4, "web安全")
    infos.append(info)

    for info in infos:

        base_url = "https://www.mukedaba.com/forum.php?mod=forumdisplay&fid=" + str(
            info[0]) + "&orderby=dateline&filter=author&orderby=dateline&page="
        page = info[1]
        prefix = "https://www.mukedaba.com/"
        f_path = u"D:\\爬取\\慕课大巴课程列表-" + str(info[2]) + "-20180316.txt"
        get_subject(base_url, page, prefix, f_path)

get_mooc()



