def work1():
	# 访问元素
	bicycles = ['trek', 'cannondale', 'redline', 'specialized']
	print(bicycles)
	print(bicycles[0])
	print(bicycles[1].title())


	# 反序输出
	names = ['logan','Erices', 'Andy']
	print(names[-1])
	print(names[-2])


	print('\n\n')
	# 倒序输出
	for x in range(1,4):
		print(names[-1*x].title())


	message = f"My first bicycles was a {bicycles[0].title()}"
	print(message)


	"""
	练习3-1：姓名 　将一些朋友的姓名存储在一个列表中，并将其命 名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓 名打印出来。

	练习3-2：问候语 　继续使用练习3-1中的列表，但不打印每个朋友 的姓名，而为每人打印一条消息。每条消息都包含相同的问候语， 但抬头为相应朋友的姓名。

	练习3-3：自己的列表 　想想你喜欢的通勤方式，如骑摩托车或开 汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系 列有关这些通勤方式的宣言，下面是一个例子。
	"""

	#3-1
	names = ["Logan", "Allen", "Andy", "Monica", "Rolls"]
	print(names[0])
	for x in names:
		print(x.title())



	print('\n\n\n')
	#3-2
	for index in range(0,len(names)):
		name = names[index]
		msg = f"Hello, {name.title()}. I am Logan, nice to met you."
		print(msg)


	print("\n\n\n")
	#3-3
	workWay = ["subway", "bus", "bicycle", "car", "walk", "home"]
	for way in workWay:
		msg = f"I am go to work by {way.title()}"
		print(msg)


# work1()


def work2():
	motorcyles = ['honda', 'yamaha', 'suzuki']
	print(motorcyles)

	motorcyles[0] = 'ducati'
	print(motorcyles)
	# list[index], insert(index,value), append(value), del list[index], pop(index,(default is lastIndex)), remove(value)


	names = []
	names.append('logan')
	names.append('Monica')
	print(names)

	names.insert(1, 'Ellen')
	print(names)


	del names[0]
	print(names)

	names.insert(0,"Logan")
	print(names)

	names2 = names.copy()

	lastName = names.pop()
	print(f"LastName is : {lastName}, And names: {names}")

	print(names2)
	indexName = names2.pop(0)
	print(indexName)

	names.remove("Ellen")
	print(names)


# work2()


def invite(guests):
	msg = f"{guests}, Would you come diner with us tomorrow？"
	print(msg)

def work3():
	"""
	　动手试一试
		下面的练习比第2章的练习要复杂些，但让你有机会以前面介 绍过的各种方式使用列表。

	练习3-4：嘉宾名单 　如果你可以邀请任何人一起共进晚餐 （无论是在世的还是故去的），你会邀请哪些人？请创建一个 列表，其中包含至少三个你想邀请的人，
	然后使用这个列表打 印消息，邀请这些人来与你共进晚餐。

	练习3-5：修改嘉宾名单 　你刚得知有位嘉宾无法赴约，因此 需要另外邀请一位嘉宾。
		以完成练习3-4时编写的程序为基础，在程序末尾添加一 条print 语句，指出哪位嘉宾无法赴约。 
		修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的 嘉宾的姓名。 
		再次打印一系列消息，向名单中的每位嘉宾发出邀请。
	练习3-6：添加嘉宾 　你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
		以完成练习3-4或练习3-5时编写的程序为基础，在程序末 尾添加一条print 语句，指出你找到了一个更大的餐桌。 
		使用insert() 将一位新嘉宾添加到名单开头。 使用insert() 将另一位新嘉宾添加到名单中间。 
		使用append() 将最后一位新嘉宾添加到名单末尾。 打印一系列消息，向名单中的每位嘉宾发出邀请。

	练习3-7：缩减名单 　你刚得知新购买的餐桌无法及时送达， 因此只能邀请两位嘉宾。
		以完成练习3-6时编写的程序为基础，在程序末尾添加一 行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。 
		使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾 为止。每次从名单中弹出一位嘉宾时，都打印一条消息， 让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。 
		对于余下两位嘉宾中的每一位，都打印一条消息，指出他 依然在受邀人之列。 
		使用del 将最后两位嘉宾从名单中删除，让名单变成空 的。打印该名单，核实程序结束时名单确实是空的。
	"""
	guests = ["Logan", "Ellen", "Ross", "Rechel"]
	invite(guests)

	print("Aha, Ellen won't come here, So")

	guests[1] = "Andy"
	invite(guests)

	guests.insert(1, "Joseph")
	invite(guests)

	guests.append("Chandler")
	invite(guests)

	print("Sorry, There are just two seat")
	guests.pop()
	guests.pop()
	guests.pop()
	guests.pop()
	invite(guests)

	del guests[0]
	del guests[0]
	invite(guests)

# work3()


def work4():
	print("This is work4")
	cars = ['bmw', 'audi', 'toyota', 'subaru']
	newCars = cars.copy()
	print(cars)
	cars.sort()

	print(cars)
	cars.sort(reverse=True)
	print(cars)

	print('\n\n\n sorted() test')
	print(newCars)
	print(sorted(newCars))
	print(sorted(newCars, reverse=True))

	newCars.reverse()
	print(newCars)


	print(len(newCars))

# work4()


def work5():
	"""
	动手试一试

练习3-8：放眼世界 　想出至少5个你渴望去旅游的地方。

将这些地方存储在一个列表中，并确保其中的元素不是按字母 顺序排列的。

按原始排列顺序打印该列表。不要考虑输出是否整洁的问题， 只管打印原始Python列表。

使用sorted() 按字母顺序打印这个列表，同时不要修改 它。 
再次打印该列表，核实排列顺序未变。 
使用sorted() 按与字母顺序相反的顺序打印这个列表， 同时不要修改它。
再次打印该列表，核实排列顺序未变。 
使用reverse() 修改列表元素的排列顺序。打印该列表， 核实排列顺序确实变了。 
使用reverse() 再次修改列表元素的排列顺序。打印该列 表，核实已恢复到原来的排列顺序。 
使用sort() 修改该列表，使其元素按字母顺序排列。打 印该列表，核实排列顺序确实变了。 
使用sort() 修改该列表，使其元素按与字母顺序相反的 顺序排列。打印该列表，核实排列顺序确实变了。
	"""
	places = ["tibet", "japan", "American", "Australia", "singapore", "tokyo", "seoul"]
	print(sorted(places))
	print(places)

	places.reverse()
	print(places)
	print(sorted(places, reverse=True))
	print(places)

	places.sort()
	print(places)
	places.sort(reverse=True)
	print(places)

# work5()

def work6():
	languages = ['english', 'japanese', 'Chinese', 'Australian', 'Italian', 'korean']
	print(languages)
	print(len(languages))
	languages.append('Russian')
	languages.insert(1, 'Portuguese')
	languages.remove('Chinese')
	print(languages)

	del languages[0]
	print(languages)

	lastLanguage = languages.pop()
	print(lastLanguage)

	languages.sort()
	print(languages)
	languages.sort(reverse=True)
	print(languages)

	print(sorted(languages))
	
work6()






