import itchat
import requests
from bs4 import BeautifulSoup
import http.cookies

'获取公众号'

itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]

username = friends[0]['UserName']
# print(friends[0])
# print(username)
# mps = itchat.search_mps(userName='@da301fe596fb340a704b531da8a3c6ef')
# for i in mps:
#     print(i)

# for i in friends[1:]:
#     uname = i['NickName']
#     m = itchat.search_mps(nickName=uname)
#
#     if m is not  None:
#         print(i['NickName'])


cookie = http.cookies.SimpleCookie()
cookie['seccodeRight'] = 'success'
cookie['SUV'] = '000C63263C15D97A5A1786C3325D5901'
cookie['SNUID'] = 'AD01C2EBD7DDB5246069D9BFD8F54410'



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
base_url = "http://weixin.sogou.com/weixin?type=1&s_from=input&query="
url_tail = "&ie=utf8&_sug_=n&_sug_type_=&w=01019900&sut=1028&sst0=1516168295016&lkt=0%2C0%2C0"
timeout = 5
s = requests.Session()

mps = itchat.get_mps()
result = []
if len(mps) > 0:
    for i in mps:
        r = {}
        # print(i['NickName'])
        url = base_url + i['NickName'] + url_tail
        # print(url)
        response = s.get(url, headers=headers, timeout=timeout)
        r['html'] = response.content.decode('utf-8')
        # print(r['html'])
        # exit()
        r['url'] = url
        r['info'] = i
        result.append(r)
        print(r['html'])
        soup = BeautifulSoup(r['html'], 'lxml')
        img = soup.find(id="seccodeImage")
        print(img)
        exit()

    # print(result)


# m2 = itchat.search_friends(nickName="小髭情调")
# m = itchat.search_mps(name="夕人")
#
# print("微信号")
# for i in m2:
#     # print(i)
#     for k, v in i.items():
#         print(str(k) + ": " + str(v))
#
# print("公众号")
# for i in m:
#     for k, v in i.items():
#         print(str(k) + ": " + str(v))