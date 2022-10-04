
import re

#rstrip函数只会去除在整个字符串末尾出现一次或多次的给定字符, 注意只限制结尾

name = 'I love Python !!'
print(name)

new_name = name.rstrip("!")
print(new_name)


new_name_2 = new_name.rstrip()
print(new_name_2)


# 去除字符串多个符号
a = "happy! New! Year!!!"
output = re.sub(r'\b!+(?!\s)', '', a)
print(output)


b = "logan"
c = 'LOGAN'
print(b.title())
print(c.lower())
print(c.upper())


