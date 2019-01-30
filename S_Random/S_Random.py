# coding=utf-8

import random
# random() 随机生成[0， 1)范围内的浮点数
a = random.random()
print(a)

# uniform() 随机生成指定范围内的浮点数
b = random.uniform(1, 100)
print(b)

# randint() 随机生成指定范围内的整数
c = random.randint(1, 100)
print(c)

# randrange() 从指定范围内，按指定基数递增的集合中 获取一个随机数。
d = random.randrange(2, 100, 2)
print(d)

# choice() 从序列中获取一个随机元素。
# 生成一个1到10的list
l = list(range(1, 10))
# 从list中随机选择一个元素
e = random.choice(l)
print(e)

# choices() 从序列中获取一组随机元素。
# 生成一个1到10的list
l = list(range(1, 10))
# 从list中随机选择一组元素
f = random.choices(l, k=6)
print(f)

# shuffle() 用于将一个列表中的元素打乱,即将列表内的元素随机排列。
l = list(range(1, 10))
# 打印生成的list
print(l)
# 将list中的元素随机排列。注意：Shuffle函数会修改原有序列，返回None
random.shuffle(l)
print(l)

# sample() 从指定序列中随机获取指定长度的片断并随机排列。注意：sample函数不会修改原有序列。
l = list(range(1, 10))
print(l)
m = random.sample(l, 5)
print(l)
print(m)


