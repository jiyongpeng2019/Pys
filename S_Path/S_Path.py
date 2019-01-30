# coding:utf-8

import os

file_path = "E:\\PyS\\S_Random\\S_Random.py"
dict_path = "E:\\PyS\\Tmp\\tmp01"
# 范围文件或目录的绝对路径
print(os.path.abspath(file_path))  # E:\PyS\S_Random\S_Random.py
print(os.path.abspath(dict_path))  # E:\PyS\Tmp\tmp01
# 返回文件或目录的路径
print(os.path.dirname(file_path))  # E:\PyS\S_Random
print(os.path.dirname(dict_path))  # E:\PyS\Tmp
# 返回文件名或目录名
print(os.path.basename(file_path))  # S_Random.py
print(os.path.basename(dict_path))  # tmp01
# 将path分割成目录和文件名二元组 或 目录和目录名二元组
print(os.path.split(file_path))  # ('E:\\PyS\\S_Random', 'S_Random.py')
print(os.path.split(dict_path))  # ('E:\\PyS\\Tmp', 'tmp01')
# 如果path存在，返回True,不存在，返回False
print(os.path.exists(file_path))
print(os.path.exists(dict_path))
#
print(os.path.isabs(file_path))
print(os.path.isabs(dict_path))

list_str = "All good things come to those who wait."
print(list_str.split(" ", 2)[2])
l = list_str.split(" ")
print("-".join(list(l)))
