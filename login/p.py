__author__ = 'thw'


import urllib.parse
import urllib.request
import re


loginurl = 'http://10.3.8.211/'

def login():

    login_data = { "DDDDD":"username",      #username is your student number
                   "upass" :"password",        #your login password
                   "0MKKey":""}
    login_data = urllib.parse.urlencode(login_data)
    print(login_data)
    login_data = login_data.encode("utf-8")
    myrequest = urllib.request.Request(loginurl,login_data)
    result = urllib.request.urlopen(myrequest)
    result =(result.read()).decode('gb2312')

    #print(result)

    if '登录成功窗' in result:
        print("登录成功")
    else:
        print("登录成功")

  

login()