# 通过位置映射
print("{} {}" .format("hello", "world"))

print("{1} {0} {1}" .format("hello", "world"))

# 通过关键字参数
print("我叫{name},我今年{age}岁" .format(age=20, name="王大锤"))

# 格式限定符 语法是{}中带:号

# 填充与对齐 填充常跟对齐一起使用
# ^ < >分别是居中，左对齐，右对齐，后边带宽度 :号后面带填充的字符，只能是一个字符，不指定的话默认用空格填充
print("{:9}".format(123))
print("{:^9}".format(123))
print("{:<9}".format(123))
print("{:>9}".format(123))

print("{:a^9}".format(123))
# 精度与类型f  其中.2表示长度为2的精度，f表示float类型。
print("{:.2f}".format(123.4))

# 其他类型 进制 b 二进制， d 十进制， o 八进制， x 十六进制
print("{:b}".format(17))
print("{:d}".format(17))
print("{:o}".format(17))
print("{:x}".format(17))

# 用，号还能用来做金额的千位分隔符。
print("{:,}".format(1234567890))

