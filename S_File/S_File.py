# coding:utf-8

import os
path_name = os.path.dirname(os.path.abspath("S_File.py"))
print(path_name)
file_path = os.path.dirname(path_name)
print(file_path)

file_name = file_path + "\\Tmp\\1.txt"
print(file_name)
f = open(file_name)
for line in f.readlines():
    if line[0] != "#":
        print(line)






