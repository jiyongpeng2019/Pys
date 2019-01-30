# coding:utf-8

# 获取帮助内建函数 help()
import sys
help(sys.getsizeof)

# 数值类型内建函数 bin() oct() hex()
# Python新版本中，二进制已0b作为前缀，八进制以0作为前缀，十六进制已0x作为前缀
print(bin(21))
print(oct(21))
print(hex(21))

# 对象生成的内建函数 int() float() complex() str() list() dict() tuple()  python3 不支持long类型
"""
int()    将数值或字符串转换为整数int，完整使用形式int(x,base),base用于指定进制
float()  将数值或字符串转换为浮点数
complex()返回一个复数，完整使用形式 complex(real,imag)
"""
print(int(21.9))
print(float(21))
print(complex(21.3, 3))
"""
str()    将所给对象转换为字符串,使用形式为str(object)
list()   获取对象，转换为列表, list(object)
dict()   获取映射转换为字典，dict(mapping)
tuple()  获取一个可迭代的对象，返回一个元组, tuple(iterable) 
"""
print(str(99))
print(list("123"))
print(dict(one=33, two=44))
print(tuple("123"))
