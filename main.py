#!/usr/bin/python
# coding:utf8



#import requests
#import base64
#import time
#import urllib3.disable_warnings
import os
from base64 import b64encode
from urllib3 import disable_warnings
from time import sleep
from requests import session
import json
print("|","*".ljust(100,"*"),"|")  # 左对齐
print("|","design by Information Center".center(100,"*"),"|") # 居中对齐
print("|","*".rjust(100,"*"),"|")  # 右对齐
print("\n\n\n\n\n\n\n\n\n\n")
disable_warnings()

online = "User is online"
ipmac = "User bound to invalid IP/MAC address"
account = "Invalid account and password"
url = "https://192.168.110.253:8080/"
session = session()
configFile = os.path.expanduser('~') + "/netconfig.txt"
userInfo = {"username":"","password":""}

def createConFile(userData):
    js = json.dumps(userData)
    file = open(configFile, "w")
    file.write(js)
    file.close()

def readConFile():
    file = open(configFile, "r")
    js = file.read()
    data = json.loads(js)
    return data



try:
    page = session.get(url, verify=False)
except:
    #抛出异常
    print("请检查你的网线是否插好!!!")
    sleep(1)
    exit()
else:
    if online in page.text:
        print("已经登录了，不用重复登录")
       # sleep(1)
        exit()

#读取配置文件，若有配置文件且用户密码正确，则直接登录
if os.path.exists(configFile):
    #如果存在,读取文件
    statuscode = 0
    data = readConFile()
    try:
        login_page = session.post(url, data=data, verify=False)
        statuscode = login_page.status_code
    except Exception as e:
        print("验证中，请稍后")
    finally:
        if statuscode == 200:
            #验证错误，删除配置文件，开始循环
            os.remove(configFile)
        else:
            print("登录成功,工作愉快")
            #sleep(1)
            exit()








#开始循环验证登录
while(1):
    statuscode = 0#初始化装填码
    userName = input("请输入用户名:").strip()
    #userName = "luozhifeng"
    userName_64 = b64encode(userName.encode("utf-8"))
    userName_64 = str(userName_64, encoding="utf8")
    userPassword = input("请输入密码:").strip()
    #userPassword = "luozhifeng"
    userPassword_64 = b64encode(userPassword.encode("utf-8"))
    userPassword_64 = str(userPassword_64, encoding="utf8")
    data = {"actionType": "umlogin",
            "language": 0,
            "password": userPassword_64,
            "password1": userPassword,
            "userIpMac": "",
            "username": userName_64,
            "username1": userName}
    try:
        login_page = session.post(url, data=data, verify=False)
        statuscode = login_page.status_code
    except Exception as e:
        print("验证中，请稍后")
    finally:
        if statuscode == 200:
            #验证错误，开始输出错误类型
            if ipmac in login_page.text:
                print("这不是本机对应的账号，请重新输入")
            elif account in login_page.text:
                print("错误的账户或密码，请重新输入")
        else:
            print("登录成功,工作愉快")
            createConFile(userData=data)
            #sleep(1)
            exit()







