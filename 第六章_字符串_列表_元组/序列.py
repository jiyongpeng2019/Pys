# coding:utf-8

# 连接操作符 +
s1 = "aaa"
s2 = "bbb"
print("连接操作符(+):%s" % s1+s2)

# 重复操作符 *
s1 = "c"
print("重复操作符(*):", s1 * 10)

# 字符串长度函数len()
s1 = "123456789"
print("字符串长度为:%s" %len(s1))

# 切片操作符 [] [:] [::] 前闭后开, 序列元素的下表（index）从零开始

s1 = "0123456789"
# 从下标零开始到下标4
print(s1[:5])
# 从下表2到最后
print(s1[2:])
# 从下表1开始到下标4
print(s1[1:5])
# 下标为5的值
print(s1[5])
# 从下表0开始到下标4，每隔2取一个元素
print(s1[0:5:2])
