def work1():
    print("Ok, Today let's learn dictionary of Python")

    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0['color'])
    print(alien_0['points'])


    alien_0['speed'] = 'slow'
    print(alien_0)
    a = alien_0.get('a', 'Not a assigned')
    b = alien_0.get('b')
    print(a,b)

def work2():
    """
    练习6-1：人 　使用一个字典来存储一个熟人的信息，包括 名、姓、年龄和居住的城市。该字典应包含键first_name 、last_name 、age 和city 。将存储在该字典中的每项信息 都打印出来。

    练习6-2：喜欢的数 　使用一个字典来存储一些人喜欢的数。 请想出5个人的名字，并将这些名字用作字典中的键；找出每 个人喜欢的一个数，并将这些数作为值存储在字典中。打印每 个人的名字和喜欢的数。为了让这个程序更有趣，通过询问朋 友确保数据是真实的。

    练习6-3：词汇表 　Python字典可用于模拟现实生活中的字 典。为避免混淆，我们将后者称为词汇表。
    想出你在前面学过的5个编程术语，将其用作词汇表中的 键，并将它们的含义作为值存储在词汇表中。 以整洁的方式打印每个术语及其含义。为此，可先打印术 语，在它后面加上一个冒号，再打印其含义；也可在一行 打印术语，再使用换行符（\n ）插入一个空行，然后在 下一行以缩进的方式打印其含义。
    """
    zhouchao = {"first_name": "zhou", "last_name": "chao", "age": 29, "city": "shenzhen"}
    print(zhouchao)

    favorite_numbers = {"monica": 12, "logan": 11, "jack": 23, "jordan": 17, "Arthur": 22}
    print(favorite_numbers)
# work2()

def work3():
    user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi'
    }

    for key, value in user_0.items():
        print(f"\nkey:{key}")
        print(f"value:{value}")

    for k, v in user_0.items():
        print(k,v)

    favorite_languages = {
        'jen': 'python',
        'sarach': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    print(favorite_languages)

    for k in favorite_languages.keys():
        print(k.title())

    for k in favorite_languages:
        print(k.title())

    friends = ['phil', 'logan']

    for name, favorite_language in favorite_languages.items():
        if name in friends:
            print(f"Hi, {name}. I see you love {favorite_language}")
        else:
            print(f"Hi, {name}.")

    if 'logan' not in favorite_languages.keys():
        print("Logan, please take our poll.")


# work3()

def work4():
    favorite_languages = {
        'jen': 'python',
        'sarach': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

    for name, favorite_language in sorted(favorite_languages.items()):
        print(f"{name}, thank you for taking the poll.")

    language = {'python', 'ruby', 'c', 'object-c'}
    print(language)

    pass
# work4()

def exercises():
    """

    练习6-5：河流 　创建一个字典，在其中存储三条重要河流及 其流经的国家。例如，一个键值对可能是'nile': 'egypt'
    使用循环为每条河流打印一条消息，下面是一个例子。
        The Nile runs through Egypt.
        使用循环将该字典中每条河流的名字打印出来。
        使用循环将该字典包含的每个国家的名字打印出来。

    练习6-6：调查 　在6.3.1节编写的程序favorite_languages.py中 执行以下操作。

        创建一个应该会接受调查的人员名单，其中有些人已包含 在字典中，而其他人未包含在字典中。
        遍历这个人员名单。对于已参与调查的人，打印一条消息 表示感谢；对于还未参与调查的人，打印一条消息邀请他 参加。
    """
    #6-5
    rivers = {"Yangtze river": "china", "nile": "Egypt", "Yellow River": "china"}
    for river, country in  rivers.items():
        print(f"The {river.title()} runs through {country.title()}.")

    #6-6
    investigative_users = ["james", "howard", "phil", "carl", "logan"]

    favorite_languages = {
        'jen': 'python',
        'sarach': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    for user in investigative_users:
        if user in favorite_languages.keys():
            print(f"{user}, thank you for taking the poll.")
        else:
            print(f"Hi, {user}. please take our poll.")

    pass
# exercises()

def work5():
    alien_0 = {'color': 'green', 'point': 5}
    alien_1 = {'color': 'yellow', 'point': 5}
    alien_2 = {'color': 'red', 'point': 5}
    aliens = [alien_0, alien_1, alien_2]
    for alien in aliens:
        print(alien)

    aliens.clear()
    for alien_number in range(30):
        new_alien = {'color': 'green', 'point': 5}
        aliens.append(new_alien)

    for alien in aliens[:5]:
        print(alien)
    pass
# work5()

def exercises_02():
    """
    create time : 2022/10/19
    @Author     : Logan_wu
    Version     : 1.0
    @emial      : 420885426@qq.com
    """
    """
    练习6-7：人们 　在为完成练习6-1而编写的程序中，再创建两 个表示人的字典，然后将这三个字典都存储在一个名 为people 的列表中。遍历这个列表，将其中每个人的所有信 息都打印出来。
    """
    user_0 = {"last_name": "Wu", "first_name": "Logan", "city": "shenzhen", "age": 31}
    user_1 = {"last_name": "green", "first_name": "rachel", "city": "NewYork", "age": 24}
    user_2 = {"last_name": "Bing", "first_name": "chandler", "city": "NewYork", "age": 26}
    peoples = [user_0, user_1, user_2]
    for user in peoples:
        full_name = f"{user.get('first_name').title()} {user.get('last_name').title()}"
        print(f"{full_name} is {user.get('age')} and live in {user.get('city')}")
    """
    练习6-8：宠物 　创建多个表示宠物的字典，每个字典都包含 宠物的类型及其主人的名字。将这些字典存储在一个名为pets 的列表中，再遍历该列表，并将有关每个宠物的所有信息都打 印出来。
    """
    pet_0 = {"name": "aJu", "owner": "logan", "type": "cat"}
    pet_1 = {"name": "Wandcai", "owner": "来福", "type": "dog"}
    pet_2 = {"name": "xiaoQiang", "owner": "5927", "type": "cockroach"}
    pets = [pet_0, pet_1, pet_2]
    for pet in pets:
        for k,v in pet.items():
            print(f"key: {k} value: {v};")
        print("\n")

    """
    练习6-9：喜欢的地方 　创建一个名为favorite_places 的 字典。在这个字典中，将三个人的名字用作键，并存储每个人 喜欢的1～3个地方。为了让这个练习更有趣些，可以让一些朋 友说出他们喜欢的几个地方。遍历这个字典，并将其中每个人 的名字及其喜欢的地方打印出来。

    """
    favorite_places = {}
    favorite_places["Logan"] = ["NewYork", "Kyoto", "seoul"]
    favorite_places["chandler"] = ["NewYork", "seattle"]
    favorite_places["Monica"] = ['London', 'Lasvegas']
    favorite_places["rachel"] = ['NewYork']
    for name, places in favorite_places.items():
        if len(places) > 1:
            all_places = " ".join([f"{v.title()}," for v in places])
            print(f"{name.title()} favorite place are {all_places[:-1]}.")
        else:
            print(f"{name.title()} favorite place is {places[0].title()} ")
    """
    练习6-10：喜欢的数2 　修改为完成练习6-2而编写的程序，让 每个人都可以有多个喜欢的数，然后将每个人的名字及其喜欢的数打印出来。
    
    练习6-11：城市 　创建一个名为cities 的字典，将三个城市 名用作键。对于每座城市，都创建一个字典，并在其中包含该 城市所属的国家、人口约数以及一个有关该城市的事实。在表 示每座城市的字典中，应包含country 、population 和fact 等键。将每座城市的名字以及有关信息都打印出来。

    练习6-12：扩展 　本章的示例足够复杂，能以很多方式进行扩 展。请对本章的一个示例进行扩展：添加键和值、调整程序要 解决的问题或改进输出的格式。
    """
    cities = {}
    cities["shenzhen"] = {"country": "china", "population": "1700W", "fact": "crowded and young"}
    cities["changsha"] = {"country": "china", "population": "1000W", "fact": "crowded , old and mean"}
    cities["xiangxi"] = {"country": "china", "population": "500W", "fact": "old and mean people"}
    for city, infos in cities.items():
        info = " ".join(infos.values())
        print(f"{city} : {info}")

    pass

exercises_02()
def test_foin():
    """
    create time : 2022/10/19
    @Author     : Logan_wu
    Version     : 1.0
    @emial      : 420885426@qq.com
    """
    result = "".join([f"{v}" for v in range(10)])
    print(result)
    pass
# test_foin()