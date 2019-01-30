# coding:utf-8

import os
import time


def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        print("不是文件或文件夹")
        return False

    if os.path.isfile(path):
        file_path = os.path.split(path)
        lists = file_path[1].split(".")
        file_ext = lists[-1]
        img_ext = ['bmp', 'jpeg', 'gif', 'psd', 'png', 'jpg']
        if file_ext in img_ext:
            os.rename(path, file_path[0] + "/" + lists[0] + "_fc." + file_ext)
            i += 1
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path, x))


# img_dir = "E:\\PyS\\S_File\\img"+
img_dir = "\\1"
img_dir = img_dir.replace("\\", "/")
start = time.time()
i = 0
change_name(img_dir)

c = time.time() - start
print("程序运行耗时：%0.2f" %c)
print("总共处理了%s张图片" %i)