# coding:utf-8
# 将list转化为字典
a = ["a", "b", "c"]
b = [1, 2, 3]
c = zip(a, b)
print(dict(c))

# 将字典转化为列表
m ={"a": 1, "b": 2, "c": 3}
"""
list1 = list(m)
print(list1)
list2 = list(m.values())
print(list2)
"""
print(list(m.keys()), end="列表Keys\n")
print(list(m.values()), end="列表Values\n")
print(tuple(m.keys()), end="元组Keys\n")
print(tuple(m.values()), end="元组Values\n")
print(str(m.keys()), end="字符串\n")
print(str(m.values()), end="字符串\n")

