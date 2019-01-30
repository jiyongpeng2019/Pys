# coding:utf-8

# r+, w+, a+
# Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
# 注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法
fo = open("a.txt", "a+")
# 打印文件名
print(fo.name)

# write() 方法用于向文件中写入指定字符串。
# 在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
n1 = fo.write("abcde")
print(n1)
fo.write("\n")
n2 = fo.write("11111\n")
print(n2)


# flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
# 一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
# fo.flush()

# 关闭文件。关闭后文件不能再进行读写操作。
fo.close()

fo = open("a.txt", "r+")
# file.read([size]) 从文件读取指定的字节数，如果未给定或为负则读取所有。
content = fo.read()
print(content)
