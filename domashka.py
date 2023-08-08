# password = input("Введите пароль: ")
# password2 = input("Введите пароль: ")


# has_upper = False
# has_lower = False
# has_digit = False
# has_special = False


# for char in password:
#     if password == password2:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         else:
#             has_special = True


# if has_upper and has_lower and has_digit and has_special and len(password)>= 8 and len(password2) >= 8:
#     print("Пароль является безопасным.")
# else:
#     print("Пароль не соответствует требованиям безопасности.") 
# str = "fergree112th"
# for i in str:
#     print(str.isdigit())


# 1. Проверка пароля (Сложность пароля): Напишите программу, которая принимает 
# пароль в виде строки и проверяет его на безопасность. Пароль должен содержать 
# хотя бы одну заглавную букву, одну строчную букву, одну цифру и один специальный 
# символ. Программа должна выводить статус безопасности пароля.


# passord1 = input("Пишите пароль: ")
# passord2 = input("Повторите пароль: ")

# t1 = False
# t2 = False
# t3 = True
# t4 = False
# if passord1 == passord2:
#    if passord2.istitle():
#        t1 = True
#    for i in passord1:
#         if i.isdigit():
#           t2 = True
#    for i in passord1:
#       if i.isalnum():
#        t3 = False
#    for i in passord1:
#       if i.islower():
#        t4 = True
#    if t1 == True and t2 == True and t3 == False and t4 == True and len(passord2)>=8:
#       print("Пароль хороший") 
#    elif t1 == True and t2 == True and t3 == False and t4 == True and len(passord2)<8:
#       print("Средний пароль")
#    else:
#       print("Плохой пароль")
# else:
#     print("пароли не совпадают ")
# print(t1,t2,t3,t4)
# 
# 3. FizzBuzz: Напишите программу, которая выводит числа от 1 до 100,
# но заменяет числа, кратные трем, на "Fizz", числа, кратные пяти, на "Buzz", 
# а числа, кратные и трем, и пяти, на "FizzBuzz".

# for i in range(1,101):
#    if i%3 == 0:
#       print("Fizz",i)
#    if i%5 == 0:
#       print("Buzz",i)
#    if i% 3== 0 and i%5 == 0:
#       print("FizzBuzz",i)
#    else:
#       print(i)


# 6. Сортировка списка: Напишите программу, которая просит пользователя ввести 
# список чисел, а затем сортирует и выводит этот список в порядке возрастания. 
# Постарайтесь не использовать встроенные функции сортировки Python.

# ch = input("пишите число:: ")
# while ch.isdigit() != True:
#    list1 = ch.split()
#    print(list1)
    
