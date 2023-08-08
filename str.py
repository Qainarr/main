#изменение текста
#text = "hello world"

#print(text.title(), "Title") # каждая завлавная буква верхнем регистре  # Hello World Title
#print(text.upper(), "Upper") # все буквы в вернем регистре            # HELLO WORLD Upper
# print(text.lower(), "Lower") # все буквы в нижнеи регистре
# print(text.capitalize(),"capitalize") # первая буква в вернем регистре 
# print(text.swapcase(),"swapcase") # переводит буквы в нижний регистре а верхний



# hello world Lower
# Hello world capitalize
# HELLO WORLD swapcase

# -----------------------------
 
#bool

# a1 = "hello123"
# a2 = "HelloWorld"
# a3 = "123456"
# a4 = "  "
# print(a3.isdigit(),"> isdigit") # Все ли состоит из цифр
# print(a2.isalpha(),"> isalpha") # Все ли состоит из букв
# print(a2.isidentifier(), "isidentifier") #Все ли слитно
# print(a2.islower(), "> islower") # Все ли у нас в нижнем регистре
# print(a1.isupper(), "> isupper") # все ли у нас в вернем регистре
# print(a1.isnumeric(), "> isnomeric") #  Все ли состоит из цифр
# print(a2.istitle(), "> istitle") # Каждая первая заглавная буква в верхнем ресистре
# print(a4.isspace(), "> isspace") # Все ли состоит из пробелов
# print(a2.isprintable(), "> isprintable") # можем ли мы это сприновать
# print(a1.isalnum(), "> isalunum") # Все ли у нас состоит из буквенно цифровых символов


#--------------------------------

#text = "  У меня дома живет кот по имени Рик  "

# print(text.strip(), "> strip") # убираем пробелы в начале и в конеце
# print(text.rstrip(), "> rstrip") # убираем пробелы в конце
# print(text.lstrip(), "> lstrip") # убираем пробелы в начале
#print(text.strip("У меня"),"> strip") #  убирает указонное символ
# print(text.lstrip(), "> lstrip") # убираем пробелы в начале


#---------------------------
# text = "Привет,     ffssd"

# print(len(text)) # считает символы

# #"ABC"
# #123
# #012 count

# # START:STOP:STEP
# #print(text[:])  #срезы

# print(text.center(25, "*")) # Центрировать текст с права и с лева
# print(text.rjust(25,"3")) #заполняет с лева 
# print(text.ljust(25,"4")) # заполняет с права


#print(text.zfill(25)) # дополнить текст с лева нулями

# name = "Kainar"
# age = "26"
# gender ="Male"

# info = f"""
# Имя: {name}
# Возраст: {age}
# Пол: {gender}
# """
# print(info)


# info = """
# Имя: {0}
# Возраст: {1}
# Пол: {2}
# """

# print(info.format(age, age, gender))




# text = "привет, fafp"
# print(text.replace("fafp","Kainar" )) #что заменить и на что заменить
# text = "Python 1C Go C# Java C++ Asambler Php"
# print(text.find("1C",8)) # ищет в строке под строку 1С с 8го индекса 
# print(text.find("1C")) # ищет по символам 
# print(text.index("1C")) #ищем в строке под 1С
# print(text.rindex("1C"))#определяем индекс в строке справа 1С

# print(text.count("1C")) # Сколько раз встречается 1С в строке

# text = "Python 123, 456. Hello"

# # print("*".join(text)) #ставить страку в под строку после каждого символа
# #print(text.split(".")) # разделить строку в под строки
# #print(text.startswith("Python", 8, 13)) #
# print(text.endswith("o"))