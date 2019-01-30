# coding:utf-8

import random
import os

print(os.path.abspath("."))
print(os.path.abspath(__file__))

L = list(range(1, 10))
random.shuffle(L)
print(L)

for i in range(len(L)):
    for j in range(len(L)-1-i):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
print(L)

M = list(range(10, 20))
print(M)
# 从List中随机获取指定长度的片段，数据存在重复
N = random.choices(M, k=7)
print(N)
# 从List中随机获取指定长度的片段，数据不重复
# N = random.sample(M, 6)
# print(N)



