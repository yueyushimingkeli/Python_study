
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

conditional_test()


