# coding:utf-8

import os
import shutil
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

exist_file = file_path + "\\Tmp\\tmp01\\2.txt"

if os.path.exists(exist_file):
    print("存在2.txt文件")
else:
    print("不存在2.txt文件")
    shutil.copyfile(file_name, exist_file)

f = open(exist_file, "w")
f.write("new file")
f.close()






