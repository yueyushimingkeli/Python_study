
# 2022年10月04日  python学习第一章 第二节学习
import sys
from io import StringIO
from email.generator import Generator
import codecs
# import this


"""
练习2-9：最喜欢的数 　用一个变量来表示你最喜欢的数，再使用 这个变量创建一条消息，指出你最喜欢的数是什么，然后将这条消 息打印出来。
练习2-10：添加注释 　选择你编写的两个程序，在每个程序中至 少添加一条注释。如果程序太简单，实在没有什么需要说明的，就 在程序文件开头加上你的姓名和当前日期，再用一句话阐述程序的 功能。
练习2-11：Python之禅 　在Python终端会话中执行命令import this ，并粗略地浏览一下其他的指导原则。

"""

#2-9

num = 21
msg = f"This is my favorite number：{num}"
print(msg)

# try 002
"""
fp = StringIO()
g = Generator(fp, mangle_from_=True,maxheaderlen=60)
g.flatten(msg)
text = fp.getvalue()
print(text)
"""


# try 003  That was not perfect But it works
# zen_of_python = codecs.encode(this.s, 'rot13')
# print(zen_of_python)

a = 1_000_000
b = 2
print(a)
print(a/b)

c = 10/3
# 左对齐 长度为10
print("{:<10.2f}abc".format(c))
print("{:<10.2f}1".format(1000))

# 右对接 长度为10
print("{:>10.2f}".format(c))
print("{:>10.2f}".format(1000))


#well done



