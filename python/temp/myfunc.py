import requests
from urllib.parse import urlparse
import  datetime
import random

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'UTF-8'
        return r.text
    except:
        return "ERROR"

def get_html_gbk(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text
    except:
        return "ERROR"
def get_root(url):
    if url:
        return urlparse(url)[0] + "://" + urlparse(url)[1]
    else:
        return ""

def genid():
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    randomNum = random.randint(0, 100)

    if randomNum < 10:
        randomNum = str(0) + str(randomNum)
    # print(datetime.datetime.now())
    # print(datetime.datetime.now().microsecond)

    id = str(now) + str(datetime.datetime.now().microsecond) + str(randomNum)
    return int(id)

# print(genid())
def get_location(url):
    r = requests.get(url, timeout=30, allow_redirects=False)
    # print(r.headers['location'])
    return r.headers['location']

def ifNullValue(v):
    return v if v else ""