# coding:utf-8

import requests

r = requests.get("http://www.cnblogs.com/yoyoketang/")
print(r.status_code)
print(r.text)
""""""
# 响应状态吗
r.status_code
# 字节方式的响应体，会自动解码gzip压缩
r.content
# 以字典对象存储服务器响应头
r.headers
# Requests中内置的JSON解码器
r.json()
# 获取URL
r.url
# 编码格式
r.encoding
# 获取cookies
r.cookies
# 返回原始响应体
r.raw
# 字符串方式的响应体，会自动根据响应头部的字符编码进行解码
r.text

par = {"Keywords": "yoyoketang"}
r_par = requests.get("http://zzk.cnblogs.com/s/blogpost", par)
print(r_par.status_code)
print(r_par.text)


