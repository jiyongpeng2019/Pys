# coding:utf-8

# abs() 函数返回数字的绝对值。
print("abs:{}" .format(abs(-22)))

# divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
print("divmod:{}" .format(divmod(3, 2)))

# max() 方法返回给定参数的最大值，参数可以为序列。
print("max:{}" .format(max(1, 3, 2, 10, 2)))
print("max:{}" .format(max([3, 56, 1])))
print("max:{}" .format(max((3, 100, 1))))
print("max:{}" .format(max("zabcdef")))

# min() 方法返回给定参数的最小值，参数可以为序列。
print("min:{}" .format(min(1, 3, 2, 10, 2)))
print("min:{}" .format(min([3, 56, 0])))
print("min:{}" .format(min((3, 100, -1))))
print("max:{}" .format(min("zabcdef")))

# pow() 方法返回 xy（x的y次方） 的值
print("pow:{}" .format(pow(2, 3)))

# 内置的 pow() 方法

# pow(x, y[, z])
# 函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
print("pow:{}" .format(pow(2, 3, 2)))
