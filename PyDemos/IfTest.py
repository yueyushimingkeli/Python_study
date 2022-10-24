import  random

print("Hello world!")
print("This is official coding by python. I'm Logan Wu Haha,This is so interesting")

def work1():
    cars = ['audi', 'bmw', 'subaru', 'toyota']
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())

# work1()

def work2():
    a = 1
    b = 2
    if  a ==1 and b == 2:
        print(a,b)
    if a == 1 or b == 2:
        print(a,b)

# work2()

def work3():
    cars = ['audi', 'haval', 'bmw']
    my_car = 'Haval'
    if my_car.lower() in cars:
        print(my_car)
# work3()

def work4():
    """
    动手试一试

练习5-1：条件测试 　编写一系列条件测试，将每个测试以及 对其结果的预测和实际结果打印出来。你编写的代码应类似于 下面这样：

    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')

    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')

    详细研究实际结果，直到你明白它为何为True 或False 。 创建至少10个测试，且其中结果分别为True 和False 的 测试都至少有5个。



    """
    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')

    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')

    my_car = 'haval'
    print("\nIs my_car == 'haval'? I predict True")
    print(my_car == 'haval')

    print("\nIs my_car == 'bmw'? I predict False")
    print(my_car == 'bmw')


    """
    练习5-2：更多条件测试 　你并非只能创建10个测试。如果想 尝试做更多比较，可再编写一些测试，并将它们加入 conditional_tests.py中。对于下面列出的各种情况，至少编写两 个结果分别为True 和False 的测试。
    检查两个字符串相等和不等。 
    使用方法lower() 的测试。 
    涉及相等、不等、大于、小于、大于等于和小于等于的数 值测试。 
    使用关键字and 和or 的测试。 测试特定的值是否包含在列表中。 
    测试特定的值是否未包含在列表中。
    """


# work4()

def conditional_test():
    my_name = 'logan'
    print(my_name == 'logan', my_name == 'jack')

    name2 = "Jack"
    print(name2.lower() == 'jack', name2 == 'jcak')

    a = 3
    b = 4
    if a > 2:
        print(f"a = {a} is big than 2")

    if b < 5:
        print(f"b = {b} is small than 5")

    if a != 5:
        print(f'a = {a} is not equal to 5')

    if a < 5 and a > 2:
        print(f'a = {a} is big than 2 and small to 5')

    if a < 5 or b < 2:
        print(f"a = {a} is small to 5 or b = {b} small to 2")

    cars = ['haval', 'audi', 'bmw', 'toyota']
    my_car = 'haval'
    if my_car in cars:
        print(f"my car {my_car} is in {cars}")

# conditional_test()



def get_color() :
    color_g = 'green'
    color_r = 'red'
    color_y = 'yellow'
    colors = [color_g, color_r, color_y]
    index = random.randint(0, 2)
    return colors[index]

def if_else_test():
    """
    动手试一试

练习5-3：外星人颜色 　假设在游戏中刚射杀了一个外星人， 请创建一个名为alien_color 的变量，并将其赋值为'green' 、'yellow' 或'red' 。

    编写一条if 语句，检查外星人是否是绿色的。如果是， 就打印一条消息，指出玩家获得了5分。 编写这个程序的两个版本，在一个版本中上述测试通过 了，而在另一个版本中未通过（未通过测试时没有输 出）。

练习5-4：外星人颜色2 　像练习5-3那样设置外星人的颜色， 并编写一个if-else 结构。

    如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5分。 如果外星人不是绿色的，就打印一条消息，指出玩家获得 了10分。 编写这个程序的两个版本，在一个版本中执行if 代码 块，在另一个版本中执行else 代码块。

练习5-5：外星人颜色3 　将练习5-4中的if-else 结构改 为if-elif-else 结构。

    如果外星人是绿色的，就打印一条消息，指出玩家获得了 5分。 如果外星人是黄色的，就打印一条消息，指出玩家获得了 10分。 如果外星人是红色的，就打印一条消息，指出玩家获得了 15分。 编写这个程序的三个版本，分别在外星人为绿色、黄色和 红色时打印一条消息。



    """

    color_g = 'green'
    color_r = 'red'
    color_y = 'yellow'
    colors = [color_g, color_r, color_y]
    alien_color = color_g

    for i in range(1,10):
        alien_color = get_color()

        if alien_color == color_g:
            print("Good job, you got 5 score")
        elif alien_color == color_r:
            print("Nice job, you got 10 score")
        else:
            print("Perfect, you got 15 score")


    """
    练习5-6：人生的不同阶段 　设置变量age 的值，再编写一 个if-elif-else 结构，根据age 的值判断一个人处于人生的 哪个阶段。

    如果年龄小于2岁，就打印一条消息，指出这个人是婴 儿。 如果年龄为2（含）～4岁，就打印一条消息，指出这个人 是幼儿。 如果年龄为4（含）～13岁，就打印一条消息，指出这个 人是儿童。 如果年龄为13（含）～20岁，就打印一条消息，指出这个 人是青少年。 如果年龄为20（含）～65岁，就打印一条消息，指出这个 人是成年人。 如果年龄超过65岁（含），就打印一条消息，指出这个人 是老年人。

    练习5-7：喜欢的水果 　创建一个列表，其中包含你喜欢的水 果，再编写一系列独立的if 语句，检查列表中是否包含特定 的水果
        将该列表命名为favorite_fruits ，并在其中包含三种 水果。
        编写5条if 语句，每条都检查某种水果是否包含在列表 中。如果是，就打印一条消息，下面是一个例子。

    You really like bananas!
    """
    age = 0
    for age in range(1,100,1):
        if age < 2:
            print("This is a baby")
        elif age >= 2 and age < 4:
            print("This is a infant")
        elif age >= 4 and age < 13:
            print("This is a child")
        elif age >= 13 and age < 20:
            print("This is a teenager")
        elif age >= 20 and age < 65:
            print("This is a adult")
        else:
            print("This is a old man")

pass


# if_else_test()

def favorite_fruit():
    """
    练习5-7：喜欢的水果 　创建一个列表，其中包含你喜欢的水 果，再编写一系列独立的if 语句，检查列表中是否包含特定 的水果
        将该列表命名为favorite_fruits ，并在其中包含三种 水果。
        编写5条if 语句，每条都检查某种水果是否包含在列表 中。如果是，就打印一条消息，下面是一个例子。

    You really like bananas!
    """
    favorite_fruits = ['banana', 'apple', 'orange', 'watermelon', 'grape', 'lemon', 'nut', 'tangerine', 'pear']
    if 'banana' in favorite_fruits:
        print("You really like banana")

    if 'peach' in favorite_fruits:
        print("You really like peach")

    if 'orange' in favorite_fruits:
        print("You really like orange")

    if 'watermelon' in favorite_fruits:
        print("You really like watermelon")

    if 'mango' in favorite_fruits:
        print("You really like mango")
    else:
        print("So you don't like mango")


# favorite_fruit()




