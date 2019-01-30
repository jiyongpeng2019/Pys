# coding:utf-8

"""Globals内容"""
# globals() 函数会以字典类型返回当前位置的全部全局变量（返回全局变量的字典)

a = "abc"
print(globals())


def f():
    b = "ccc"
    print(locals())


# locals() 函数会以字典类型返回当前位置的全部局部变量（返回局部变量的字典)
f()

