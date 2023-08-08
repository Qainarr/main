# my_list = list(range(10, 20))
# print(my_list)

# for while

#Start, Stop, Step
#range(10, 20)

# a = [1,2,3,4,5,6]
# b = []
# c =[]
# for i in range(1,101):
#     print(i, end=" ")
#     if i % 2 == 0:
#         b.append(i)
#     else:
#         c.append(i)

# print(sum(b))
# print(sum(c))
#\n переход строки parsmodul
#\t на один тап вперед

# for name in "Kainar":
    # print(name, end=" ")


# for name in "Kainar":
#     n = input("Введите имя: ")
#     print(name)


# n = [i for i in range(1,11) if i % 2 == 0] 
# print(n)

#for name in 

# users = {
#     "marselle": 20,
#     "user": 40,
# }

# for k, v in users.items():
#     print(k,v)


# for k in users.keys():
#     print(k)

# for v in users.values():
#     print(v)
 
# a = 10

# while a >= 1 :
#     print("Hello, a")
#     a = a - 1


# for i in range(1, 11):
#     if i %2 == 0:
#         print(i)
#     else:
#         continue

# while True:
#     num = int(input("напиши мне число"))
#     if num >= 10:
#         print(num)
#     else:
#         break



# while True:
# #     n = input("Напиши что-то ")

users = {
    "admin": {
        "name": "admin",
        "password": "12312312",
        "phone ": "+77058222090",
        "balance": 100,
    } 
        
}

key = None
while True:
    table = input("""
    1 Зарегистрироваться
    2 Авторизоваться
    3 Перевод баланса
    4 Информация
    5 Выйти       
>>>""")
    if table == "1":
        username = input("Придумайте поль-кое имя: ")
        name = input("Введите имя: ")
        phone = input("Введите номер тел: ")
        password = input("придумайте пароль: ")
        password1 = input("повторите пароль: ")

        while password != password1 or len(password1) < 8:
            password = input("придумайте пароль: ")
            password1 = input("повторите пароль: ")
        
        users[username] = {
            "name": name,
            "password":password1,
            "phone_number": phone,
            "balance": 100,
    }
        key = username
        print("вы уже зарегистрированы")
    elif table == "2":
        if key is None:
            """авторизация"""
            username = input("Введите поль-кое имя: ")
            password = input("Введите пароль: ")
            if username in users and password == users[username]["password"]:
                key = username
                print("Вы вошли в аккаунт", username)
            else:
                key = None
                print("Логин или пароль не верный")
        else:
            print("Вы уже авторизованы")
    elif table =="3":
        if key is not None:
            recipient_login = input("Введите логин получателя: ")
            summa = int(input("Введите сумму: "))
            # balance = 100
            if summa <= users[key]["balance"]:
                users[key]["balance"] -= summa
                users[recipient_login]["balance"] += summa
                print("Транзакция прошла успешно")
            else:
                print("у вас нет столько денег") 
        else:
            print("Вы не авторизованы") 

#1

# for r in range(1,11):
#     print(r)

#2

# k = 0
# for i in range(1, 11):
#     k += i
# print(k)

#3

# for i in range(1, 6):
#     print(i * i)

#4


# for i in "Python":
#     print(i, end= " ")

# Вывести каждую вторую букву из слова "Python":




# for i in range(0,len("Python"),2):
#     print("Python"[i])


# Посчитать сумму чисел от 1 до n, где n вводится пользователем:

# a = int(input("Введите число: "))
# nm = 0
# for i in range(1,a+1):
#     print(i)
#     nm += i
# print(nm)

# Проверить, является ли число простым 
# (простым называется число, которое делится только на 1 и само себя):
# n = int(input("Напиши число: "))
# count = True
# for i in range(2, n):
#     if n % i ==0:
#         count = False
#         break
# if count:
#     print("Простое")
# else:
#     print("Не простое")



# 7
# 1, 2, 3, 4, 5, 6, 7
# n = int(input()) # 3
# faktorial = 1
# for i in range(1, n+1): #  3
#     if n > 1:
#         faktorial *= i

#         print()


# print("Факториал числа", f"{n} == {faktorial}")


# Посчитать факториал числа n, где n вводится пользователем:

# chislo = int(input("введите число: "))
# n = 1
# for i in range(1,n+1):
#     n=n*i
# print(chislo)


# Вывести таблицу умножения от 1 до 10 для заданного числа n:

# a = int(input())
# for i in range(1, 11):

#     print(f"{a}*{i}=", a*i)



# Вывести среднее арифметическое чисел, 
# вводимых пользователем, пока не будет введен 0:

# a = int(input())
# while True: 
#         if a != 0:
#                 print(a+a)    


