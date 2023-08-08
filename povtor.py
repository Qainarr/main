# my_str = "Привет Андрей"
# print(my_str.lower()) # нижний регистер
# print(my_str.title()) # начальные буквы в верхнем регистре 
# print(my_str.upper()) # все вверхний регистор
# print(my_str.swapcase()) # маленьние буквы в большое
#                         # все большыие в маленькое
# print(my_str.capitalize()) #начальную букву верхний регистер

# string = input("напиши свое имя: ") # input это функция которая принемает в  типе str
# if string.upper() == string:
#     print("Привет") 
# else:
#     print("А мы знакомы!")

# str2 = input("напиши что то: ")
 
# print(str2.isdigit()) #ВСЕ ЛИ СОСТОИТ ИЗ ЦИФР
# print(str2.isalpha()) #ВСЕ ЛИ СОСТОИТ ИЗ БУКВ
# print(str2.isidentifier()) #все ли пишется слитно

# print(str2.islower()) # все ли в нижнем  регисторе если да то True
# print(str2.isupper()) # все ли в верхнем регисторе если да то True
# print(str2.istitle()) # везде ли заглавное буква
# print(str2.isspace()) # везде ли пробелы
# print(str2.isnumeric()) #ВСЕ ЛИ СОСТОИТ ИЗ ЦИФР
# print(str2.isprintable()) # можем ли мы это спринтовать

# text = " привет Андрей "

# print(text.strip()) # удаляет пробелы с лева и с право
# print(text.rstrip())# удаляет пробелы с лева
# print(text.lstrip())# удаляет пробелы с право
# print(text.split()) # разделяет и обарачивает в список
# print(text.partition("привет")) # разделяет и обарачивает в tuple

# text = "привет Андрей"
# a = f""""   
# input: hello       Взять значение переменной text и вставить в наш текст
#                    с помощью {text}  скобок     
# output:  {text}    форматирование строки f строка
# """
# print(a)

# text = "привет Андрей"
# a = """"  
#  input: hello              заполнение текста с поощью индексов {0} {1}т.д 
#                            для заполнение используем метод format 
#  output:  {0} {1} {2} {3}  и внутри формата указываем чем заменить индекс
# """ 
# print(a.format(text,"ttt",111, [1,2,3]))

# h = "hello 111"
# print(h.replace("1","*")) # что заменить и на что заменить
# print(h.startswith("hello")) # начинается ли наш текст с слова "hello"
# print(h.endswith("111"))     # оканчивается ли наш текст с 111
# print("*".join(h)) # после каждого символа  вставить *

# f = "GGG"
# print(f.center(5, "*")) # дополнить текст до 20 индексов с помощью *
# print(f.rjust(15,"*"))  # дополнить текст до 20 индексов с помощью * c лево
# print(f.ljust(15,"*"))  # дополнить текст до 20 индексов с помощью * с право

# # print(f.zfill(20))  # дополнить текст до 20 индексов с помощью 0 (0=const) c лево
# str1  = "222234"
# print(str1.count("2"))
# print(str1.find("8"))
# g = "привет Андрей"

# v = (g[::-1])
# s = v[::-1]
# print(s)

# TUPLE

# g = tuple()
# g = ()
# g = 1, 2,
# print(g[1])




