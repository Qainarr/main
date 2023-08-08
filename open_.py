# NAME_AGE1 = 123    const

#OPEN()
            #name file & pars mode
# file = open("text.txt", "w") #pars mode "w"
# file.write("hello world")
# file.close()


# name = input("напиши имя: ")
# # ParsMode w: Очистить и записать
# file = open("text.txt", "w") #pars mode "w"
# # write принимает только  str
# file.write(name)
# file.close()




# ParsMode Add - "a": Добавить текст не очищает 
# file = open("text.txt", "a") #pars mode "w"
# file.write("Hello\n") # перенос \n
# file.close()


# ParsMode Read - "r": Прочитать 
# file = open("text.txt", "r") #pars mode "w"
# src = file.read() # 
# file.close()

# print(src.split()) # можно приминить методы str

# with open("text.txt", "r") as file: # дать ему посвм
#     src =  file.read()
# print(src)

# Режим  текста
# r      - Только для чтения.
# w      - Только для записи. Создаст новый файл, 
#           если не найдет с указанным именем.

# a      - Откроет для добавления нового содержимого. 
#         Создаст новый файл для записи, если не найдет с указанным именем.

# rb  - Только для чтения (бинарный).
# wb  - Только для записи (бинарный). 
#        Создаст новый файл, если не найдет с указанным именем.


# with open("text.txt","r") as txt:
#     f = txt.read()
#     print(len(f.split()))

# with open("text.txt","r") as txt:
#     f = txt.read()
#     list1 = []
#     for i in f:
#         if i.isnumeric():
#             list1.append(int(i))
            
#     set1 = set(list1)
#     print(set1list1)
        
# with open("text.txt","r") as txt:
#     f = txt.read()
#     for i in f:
#         if i.isdigit():

# with open("text.txt","r") as txt:
#     f = txt.read()
#     for i in f.split():
#         if i.startswith("a") or i.startswith("A"):
#             print(i)



# Напишите программу, которая 
# считывает файл и выводит количество строк 
# в этом файле. Для решения задачи нужно использовать цикл for.

    
# with open("text.txt","r") as txt:
#     f = txt.read()
#     d = 0
#     for i in f.split():
#         d += 1
#     print(d)



# Напишите программу, которая считывает файл и 
# выводит те строки, которые содержат число.
# Для решения задачи нужно использовать for, 
# if и метод строки .isdigit().

# with open("text.txt","r") as txt:
#     aa = txt.read()
#     for i in aa.split():
#         if i.isdigit():
#             print(i)              
        

# Напишите программу, которая считывает файл и 
# выводит длину самой длинной строки. 
# Для решения задачи нужно использовать for.


# with open("text.txt","r") as txt:
#     aa = txt.read()
#     ss = 0  
#     for i in aa.split():
#         if len(i)>ss:
#             ss = len(i)
#     print(ss)    




# Напишите программу, которая считывает файл и 
# выводит на экран только те строки, которые 
# содержат восклицательный знак. 
# Для решения задачи нужно использовать for, if.

# with open("text.txt","r") as txt:
#     aa = txt.read()
#     for i in aa.split():
#         if i.count("?") or i.count("!"): 
#             print(i)

