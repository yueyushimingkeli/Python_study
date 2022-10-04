"""
练习2-3： 个性化消息 　用变量表示一个人的名字，并向其显示一 条消息。 例如： Hello Eric, would you like to learn some Python today?

练习2-4：调整名字的大小写 　用变量表示一个人的名字，再以小 写、大写和首字母大写的方式显示这个人名。

练习2-5：名言 　找一句你钦佩的名人说的名言，将其姓名和名言 打印出来。输出应类似于下面这样（包括引号）。 Albert Einstein once said, “A person who never made a mistake never tried anything new.”

练习2-6：名言2 　重复练习2-5，但用变量famous_person 表示名 人的姓名，再创建要显示的消息并将其赋给变量message ，然后打 印这条消息。

练习2-7：剔除人名中的空白 　用变量表示一个人的名字，并在其 开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。打印这个人名，显示其开头和末尾的空白。然后，分别使用剔除函 数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果 打印出来。
"""


name = 'logan'
print(f"{name}, would you like to learn some Python today?")


name = "Eric"
name = name.title()
print(f"{name}, would you like to learn some Python today?")

msg = "would you like to learn some Python today?"

name = name.lower()
print(f"{name}, {msg}")
print(f"{name.upper()}, {msg}")


famous_msg = "Albert Einstein once said, “A persion who never made a mistake never tried anything new”"
print(famous_msg)

famous_msg_2 = "Albert Einstein once said, \"A persion who never made a mistake never tried anything new\""
print(famous_msg_2)


first_name = 'albert'
last_name = 'Einstein'
famous_said = f"{first_name.title()} {last_name.title()} once said, \"A persion who never made a mistake never tried anything new.\""
print(famous_said)


name = " logan "
print(f"{name} \n")
print(f"{name.strip()} \n{name}")
print(f"{name.rstrip()}, haha")
print(f"{name.lstrip()}, haha")

str_1 = "testesteste"
str_2 = "test"
print(f"\t\t{str_1} \n \t{str_2}")
