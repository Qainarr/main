# import my_code
# print(my_code.name)

# from my_code import name, age
# print(name)
 
# from  import *

# from core.my_code import name,age
# print(name)\\
# import core.my_code
# print(core.my_code.name)



#ВСТРОЕННЫЕ МОДУЛИ
# from datetime import datetime

# date = datetime.now() #Возвращает текущию дату и время
# date = datetime.today() #Возвращает текущию дату и время

# print(date)
# print(date.time())
# print(date.date())
# print(date.year)
# print(date.day)
# print(date.hour)
# print(date.minute)
# print(date.second)
# print(date.month)


# from datetime import date

# p = date.today()
# print(p.today())
# print(p.year)
# print(p.month)
# print(p.day)

# from datetime import time
# time1 = time(13,24,57) #сами указываем время
# print(time1)
# print(time1.hour)
# print(time1.minute)
# print(time1.second)

# from datetime import datetime, timedelta

# now = datetime.now()
# print(now)

# day5 = now + timedelta(days = 5)
# print(day5)


# from datetime import datetime
# now = datetime.now()
# print(now)

# fdate = now.strftime("%Y:%m:%d %H:%M:%S") #STR
# print(fdate)

# pdate = datetime.strptime("2023-08-07 19:40","%Y-%m-%d %H:%M") #DATE
# print(pdate)

# from time import time, sleep, gmtime, strftime
# time() #1970

# print("Начало")
# sleep(5)
# print("end")


# st = gmtime()
# print(st.tm_hour +6) #Time Zone = +0
# print(st.tm_min) #Time Zone = +0

# ft = strftime("%Y-%m-%d %H:%M",gmtime())
# print(ft)

# from random import random, randint, choice
# r = random()
# print(r)

# r = randint(1,10)
# print("Случайное целое число между 1 и 10",r)
# from random import random, randint,\
# choice,shuffle, sample, choices

# users = ["Zere","Ruslan","Said","Temirlan","Nur","Abylai",
#          "Kainar", "Iskender","Bakhyt","Algat"]

# print(choice(users))
# shuffle(users)
# print(users)
# print(sample(users,5))
# print(choices(users,k=5))

# from calendar import calendar, month,weekday, weekheader
# w = weekday(2023, 8, 7)
# w = weekheader(9)
# cal = month(2023, 8, w = 9,l=4)
# cal_all =  calendar(2023)
# print(w)

# from os import system, mkdir, rename, remove
# from sys import


# for i in range(1,5):
#     system(f"rm -rf {i}")
# system("whoami")

# import sys
# print(sys.path)
# print(sys.api_version)
# print(sys.builtin_module_names)

# 1 Обработка даты и времени:
# Создайте функцию, которая принимает строку в формате 
# "YYYY-MM-DD" и возвращает день недели, 
# на который приходится эта дата.

# from datetime import datetime
# from calendar import weekday


# year = int(input("Год: "))
# month = int(input("месяц: "))
# day = int(input("день: "))

# index_weekend = weekday(year,month, day)
# we = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# print(we[index_weekend])

# 2 Работа с временем:
# Создайте таймер обратного отсчёта. 
# Пользователь вводит количество секунд, 
# и программа отсчитывает это время, 
# выводя оставшееся количество секунд 
# каждую секунду, пока время не истечет.



# from time import time, sleep, gmtime, strftime
# s = int(input())
# while s > 0:
#     s=s-1
#     sleep(1)
#     print(s)


# 3 Случайные числа и выбор элементов из списка:
# Напишите программу, которая случайным образом выбирает 
# 3 уникальных пользователя из списка users и печатает их имена.

from random import sample, choices

users = ["Zere","Ruslan","Said","Temirlan","Nur","Abylai",
         "Kainar", "Iskender","Bakhyt","Algat"]
print(sample(users,3))


llllllll = 12

fff=11