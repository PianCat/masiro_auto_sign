#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: index_ql.py(Masiro签到)
Author: PianCat & Gedley
cron: 0 30 8 * * *
new Env('Masiro签到');
Update: 2023/12/4
"""
import io
import sys
import os
import urllib.request
import requests
import re
import notify

headers_post = {
    'Host': 'masiro.me',
    'Connection': 'keep-alive',
    'Content-Length': '104',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-CSRF-TOKEN': '',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; MI 5;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://masiro.me',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://masiro.me/admin/auth/login',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}
headers_get_1 = {
    'Host': 'masiro.me',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; MI 5;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'dnt': '1',
    'X-Requested-With': 'mark.via',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}
headers_get_2 = {
    'Host': 'masiro.me',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'X-XSRF-TOKEN': '',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; MI 5;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://masiro.me/admin',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}
headers_get_3_1 = {
    'Host': 'masiro.me',
    'Connection': 'keep-alive',
    'Accept': 'text/html, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; MI 5;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://masiro.me/admin',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}
headers_get_3 = {
    'Host': 'masiro.me',
    'Connection': 'keep-alive',
    'Accept': 'text/html, */*; q=0.01',
    'X-CSRF-TOKEN': '',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; MI 5;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://masiro.me/admin',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}
headers_get_4 = {
    'Host': 'masiro.me',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; MI 5;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://masiro.me/admin',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}
doThumbUp_data = {
    'id': '',
    'type': '1',
    '_token': ''
}


def login(_name: str, _password: str):
    session = requests.session()
    url = "https://masiro.me/admin"
    session.get(url=url, headers=headers_get_1, allow_redirects=False)
    url = "https://masiro.me/admin/auth/login"
    res = session.get(url=url, headers=headers_get_1, allow_redirects=False)
    _token = re.findall('<input type="hidden" name="_token" value="(.*?)">', res.text)[0]
    headers_post["X-CSRF-TOKEN"] = _token
    headers_get_3["X-CSRF-TOKEN"] = _token
    doThumbUp_data['_token'] = _token
    data = {"username": _name, "password": _password, "activationcode": "", "_token": _token}
    url = "https://masiro.me/admin/auth/login"
    session.post(url=url, data=data, headers=headers_post, allow_redirects=False)
    headers_get_1['Referer'] = 'https://masiro.me/admin/auth/login'
    return session


def home(session):
    url = "https://masiro.me/admin/"
    session.get(url=url, headers=headers_get_1, allow_redirects=False)
    headers_get_1['Referer'] = 'https://masiro.me/admin'
    headers_get_2['Referer'] = 'https://masiro.me/admin'
    headers_get_3['Referer'] = 'https://masiro.me/admin'
    headers_get_2['X-XSRF-TOKEN'] = urllib.request.unquote(session.cookies.get('XSRF-TOKEN'))
    url = "https://masiro.me/admin/randomNovel"
    session.get(url=url, headers=headers_get_2, allow_redirects=False)
    url = "https://masiro.me/admin/checkAnnouncement"
    session.get(url=url, headers=headers_get_3_1, allow_redirects=False)
    return session


def checkAnnouncement(session):
    url = "https://masiro.me/admin/checkAnnouncement"
    session.get(url=url, headers=headers_get_3, allow_redirects=False)
    return session


def dailySignIn(session):
    url = "https://masiro.me/admin/dailySignIn"
    res = session.get(url=url, headers=headers_get_4, allow_redirects=False)
    print(res.json()['msg'])
    headers_get_2['X-XSRF-TOKEN'] = urllib.request.unquote(session.cookies.get('XSRF-TOKEN'))
    url = "https://masiro.me/admin/myNotice"
    session.get(url=url, headers=headers_get_2, allow_redirects=False)
    return session


def userCenterShow(session):
    url = "https://masiro.me/admin/userCenterShow"
    res = session.get(url=url, headers=headers_get_1, allow_redirects=False)
    a1 = re.findall('<span class="user-lev">(.*?)</span>', res.text)[0]
    a2 = re.findall('经验值:<span class="exp">(.*?)</span>', res.text)[0]
    a3 = re.findall('资历:(.*?)天', res.text)[0]
    a = f"等级: {a1}, 经验值: {a2}, 资历: {a3}天"
    print(a)
    headers_get_3['Referer'] = 'https://masiro.me/admin/userCenterShow'
    headers_get_1['Referer'] = 'https://masiro.me/admin/userCenterShow'
    return session, a

def logout(session):
    url = "https://masiro.me/admin/auth/logout"
    session.get(url=url, headers=headers_get_1, allow_redirects=False)
    return 0

class DualOutputStream:
    def __init__(self):
        self.terminal = sys.stdout
        self.mem = io.StringIO()

    def write(self, message):
        self.terminal.write(message)
        self.mem.write(message)

    def flush(self):
        # 这个方法是为了兼容 sys.stdout 的 flush 方法
        self.terminal.flush()

    def getvalue(self):
        return self.mem.getvalue()

def main(_name: str, _password: str):
    captured_output = DualOutputStream()
    sys.stdout = captured_output
    session = login(_name, _password)
    session = home(session)
    session, msg = userCenterShow(session)
    session = checkAnnouncement(session)
    session = home(session)
    session = dailySignIn(session)
    session = checkAnnouncement(session)
    session = home(session)
    logout(session)
    sys.stdout = sys.__stdout__  # 恢复标准输出到原来的状态
    content = captured_output.getvalue()  # 获取捕获的输出
    title = 'Masiro签到'
    notify.serverJ(title, content)

def handler(event, context):
    for user_pwd in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "login.txt")):
        user_pwd = user_pwd.rstrip('\n').split()
        # print(user_pwd, type(user_pwd))
        username = user_pwd[0]
        password = user_pwd[1]
        main(username, password)

if __name__ == '__main__':
    handler('event', 'context')
