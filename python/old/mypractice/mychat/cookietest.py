import http.cookiejar
from urllib import request
import http.cookies


# filename='cookie'
# cookie = http.cookiejar.LWPCookieJar(filename)
# try:
#     cookie.load(ignore_discard=True)
# except IOError:
#     print('Cookie未加载')
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
#                          '(KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
#            "Host": "http://weixin.sogou.com",
#            "Referer": "http://weixin.sogou.com/",
#            }
#
# opener = request.build_opener(request.HTTPCookieProcessor(cookie))
# opener.addheaders = [(key, value) for key, value in headers.items()]

cookie = http.cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)

cookie = http.cookies.SimpleCookie()
cookie['seccodeRight'] = 'success'
cookie['SUV'] = '000C63263C15D97A5A1786C3325D5901'
cookie['SNUID'] = 'AD01C2EBD7DDB5246069D9BFD8F54410'

