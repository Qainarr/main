# a = frozenset("rrrrdds")
# print(a)

# DICT

# my_set ={1,}
# my_dict = {
#     "name":"Marselle",
#     "age": 20,
# }
# print
# print(my_dict["age"])
# print(my_dict["name"])

# users = {
#     "kainar":{
#         "name": "kainar",
#         "num":87058222090,
#         "age":26,
#         "adress": {
#             "city": "almaty",
#             "dom":44,
#             "street": "alma city"
#                         }
#     }
# }
# print(users["kainar"]["adress"]["street"])
# my_dict = {
#     "name":"Kainar"
# }
# print(
#     my_dict.items() #Вернуть все ключи и значении в формате лист каждый элемент в тюпле
# )
# print(
   
#     my_dict.keys()  #вернуть все значение  
# )
# print(
#     my_dict.values()   # вернуть все значение в формате списка
# )

# my_dict = {

#     "name":"Kainar",
#     "color": "red"
#     }
# test = {
#     "age":20,
#     "login": {
#         "name1": "marselle",
#         "name2": "aba",
#     }
#     }
# my_dict.update(test["login"])
# print(my_dict)


# my_dict = {
#     "name":"Kainar",
#     "color": "red"
#     }

# my_dict.update({
#     "h":123,
# })
# print(my_dict)

# a = {
#     "name":"kainar"
# }

# a["name"] = 123 # Изменить значение ключа cart2 на 123
# a["aaa"] = "sss" #создать ключ "aaa" с значением "sss"
# a.update(ff=33) #создать ключ "aaa" с значением "sss"
# print(a)

# set = {1,2,3,4,5,6,7}
# set.remove(7)
# print(set)


# set1 = {1,"a",2,3,6,7}
# set2 ={9,8,8,"a"}

# # print(set1.intersection(set2))

# set3 = {1,2,3,4,5,6,"d"}
# print(set3.difference(set2))


# set1 = {"a","d",1,2,3}
# print(set1)
# set1.add("e")
# a=set1.pop()
# print(a)
# print(set1)

# dict1 = {
#     "besh_barmak":"130 сом",
#     "lagman":"135 сом",
#     "борщ":"150 com",   
# }
# # dict1["lagman"]="200 com"
# # dict1.pop("борщ")\
# dict1["drinks"]=["cola","sprite","fanta"]
# print(dict1)

set1 = {"add","clear","copy","difference","pop","intersection"}
set2 = {"update","values","clear","pop"} 

print(set1.intersection(set2))
