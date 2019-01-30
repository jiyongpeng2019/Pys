# coding:utf-8

str = input("请输入字符串:")
print(str)

fp = open("str.txt", "w")
u = str.upper()
fp.write(u)
fp.close()