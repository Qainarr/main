# SET


# type_list= [3, 2, 1]
# type_set = list(set(type_list)) #сет может сортировать все


# print(type_list)
# print(type_set)

# a = {1,}
# # b = set("h")
# print(a)
# a.
 
# a = {1,2,3,99}
# b = {1,2,3,4,5,6,7}

# # print(a.isdisjoint(b)) # не пересекается True не пересекаетсе False 

# # print(a.union(b))

# print(a.intersection(b)) # возвращает пересечение
# print(a & b)# возвращает пересечение

# print(a.difference(b)) #разность
# print(b.difference(a))#разность
# print(b - a)#разность

# print(a.symmetric_difference(b)) # симметрическая разность
#
# a = {1,3,4}
# b = a.copy()

# print(b)
# print(a)

# my_set = {1,}

# my_set.add(2)
# my_set.add("my text")
# my_set.add(False)

#print(my_set)

# my_set.remove(1)
# my_set.pop()
# my_set.clear()
# my_set.add(1)
# print(my_set)


baza_product_name = ["banan","apple","orangre","mango"]
baza_key_admun = []

table = input("""
Товары: 1
Удалить товар: 2
Добавить товар: 3
Админка: 4
выход: 5
 >>> 
""")

if table == "1":
    print("все товары", baza_product_name)
elif table == "2":
    name = input("ВВедите название товара: ")
    baza_product_name.remove(name)
    print(baza_product_name)
elif table =="3":
        name = input("ВВедите название товара: ")
        baza_product_name.append(name)
        print(baza_product_name)
elif table == "4":
     print("Функция пока не доступна")
elif table == "5":
     pass
else:
     print("такой команды нет")

# list = ["1","2","3","4","5"]
# print(list)

# tuple = ("aa","bb","cc")
# print(tuple[0])
# print(tuple[1])
# print(tuple[2])

# list = ["aa","rr", "dd"]
# list.append(1)
# list.append(1)
# list.append(1)
# list.append(1)
# list.append(1)
# print(list)

# list = ["MArselle","Aba","Aaa","ddd","ddd"]
# b = " + + ".join(list)

# print(b)

# list_1 = [1,2,3,4,5]
# list_2 = [0,98,89,98,6]
# list_1.extend(list_2)
# print(list_1)

# list = ["Jack","Jack","Jack","Jack","Jack"]

# print(list.count("Jack"))

# list = ["Oskar","Oskar",1,2,3,4]
# list.remove("Oskar")
# list.remove("Oskar")
# print(list)

# list1 = []
# a = input("напишите имя: ")
# list1.append(a)
# b = int(input("Год рождения: "))
# list1.append(b)
# c = (input("Любимый язык программирования : "))
# list1.append(c)
# print(list)

# list1 = ["rere","www","loop"]
# b = (list1.index("loop"))
# list1.pop(b)list1[1]*list1[2]
# print(list1)

# list1 = [1,2,3,4,5]
# b = list1[0]*list1[1]*list1[2]*list1[3]*list1[4]
# print(b)
# a = "3 nn 5"
# b = a.split()
# numbers = []
# letters = []
# if b[1].isdigit():
#     numbers.append(b[1])
# print(numbers)


