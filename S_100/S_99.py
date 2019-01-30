# coding:utf-8

import os
import string
cur_path = os.path.abspath("S_99.py")
print(cur_path)
p_path = os.path.dirname(cur_path)
print(p_path)

f1 = open(p_path + "\\文件\\a.txt")
a = f1.read()
print(a)
f1.close()

f2 = open(p_path + "\\文件\\b.txt")
b = f2.read()
print(b)
f2.close()

f3 = open(p_path + "\\文件\\c.txt", "w+")
l = list(a + b)
l.sort()
s = '-'
s = s.join(l)
f3.write(s)
f3.close()


