# int1 = int(input("Введите число: "))
# if int1 == 0:
#     print("Введите число")

# elif int1 % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")




# Напишите программу, которая выводит числа от 1 до 100, но заменяет числа, кратные трем, на "Fizz", 
# числа, кратные пяти, на "Buzz", а числа, кратные и трем, и пяти, на "FizzBuzz".

# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i,"FizzBuzz")
#     if i%3 == 0:
#         print(i,"Fizz")
#     if i%5 == 0:
#         print(i,"Buzz")
#     else:
#         print(i)
    






# Символы в строке: Напишите программу, которая просит пользователя ввести строку, 
# а затем выводит словарь, где каждый ключ - это уникальный символ из строки,
# а значение - это количество раз, которое символ появляется в строке.

# count
# str = input("")
# list1 = {}
# for i in str:
#     b = str.count(i)
#     dict1={
#             i : b
#          }
#     list1.update(dict1)
# # print(i,b)
# print(list1)

# my_string = "Hello, Python!"

# # Используем цикл for и метод isalpha() для подсчета букв в строке
# letter_count = 0
# for char in my_string:
#     if char.isalpha():
#         letter_count += 1
#         print(char)
# print("Количество букв в строке:", letter_count)

my_list = [1, 2, 3, 4, 5]

# Используем цикл for и метод append() для создания нового списка, содержащего квадраты элементов
squared_list = []
for item in my_list:
    squared_list.append(item ** 2)

print("Список квадратов элементов:", squared_list)
