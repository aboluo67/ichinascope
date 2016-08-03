# coding=utf8
import sys

if sys.version < "3":
    reload(sys)
    sys.setdefaultencoding("utf-8")
import time
import base64
from hashlib import sha1
from hmac import new as hmac
import json
import tick
from pymongo import MongoClient

if sys.version > "3":
    from urllib import request as http
else:
    import urllib2 as http


def create_token(access_key, secret_key):
    t = str(time.time())

    if sys.version > "3":
        token = base64.encodebytes(hmac(
            bytearray("%s,%s,%s" % (access_key, t, secret_key), "utf-8"), digestmod=sha1).digest())[:-1]
    else:
        token = base64.encodestring(hmac("%s,%s,%s" % (access_key, t, secret_key), digestmod=sha1).digest())[:-1]

    return t, token


def stock_search():
    access_key = '1e9668836f2395fc0e3918ad83bcb1eb'
    secret_key = '6364lRCtY6yg3A+CZmq1nn8DFnY='
    t, token = create_token(access_key, secret_key)

    header = {
        "access_key": access_key,
        "t": t,
        "token": token,
    }

    for i in tick.tick:
        print i
        try:
            url = "http://api.ichinascope.com/api/hq/stock/price/daily?codes=" + i +"&adjusted=f&from=2016-08-02&to=2016-08-03"
            # url = "http://api.ichinascope.com/api/hq/stock/price/daily?codes=000001&adjusted=f&from=2016-07-22&to=2016-07-26"
            req = http.Request(url, headers=header)

            data = http.urlopen(req).read()
            if isinstance(data, bytes):
                result = json.loads(data.decode("utf-8"))
            else:
                result = json.loads(data)

            conn = MongoClient('localhost', 27017)
            conn.db.data2016.insert(result['message'])
        except:pass
    return result["message"], result["type"]


print stock_search()