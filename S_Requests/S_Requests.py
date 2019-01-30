# coding=utf-8

import requests

kw = {"wd": "Python"}

post_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "30",
    "Content-Type": "application/x-www-form-urlencoded",
    # "Cookie": "jeesite.session.id=f77137cb211444ce8690e4e96ccbda3c;"
    # "pageNo": "1",
    # "pageSize": "15",
    "Hm_lvt_82116c626a8d504a5c0675073362ef6f":"1548139688,1548139811,1548142833,1548147437",
    "Hm_lpvt_82116c626a8d504a5c0675073362ef6f":"1548148439",
    "Host": "192.168.34.249:8080",
    "Origin": "http://192.168.34.249:8080",
    "Referer": "http://192.168.34.249:8080/IntensiveTest/user/login",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}
postdata = {
    "username": "zz001",
    "password": "123456",
}
r_post = requests.post("http://192.168.34.249:8080/IntensiveTest/user/login", data=postdata, headers=post_headers)
print(r_post.status_code)
print(r_post.url)
print(r_post.headers)


r_get = requests.get(r_post.url)
print(r_get.status_code)
print(r_get.text)

