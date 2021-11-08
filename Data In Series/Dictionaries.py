# -------------------------------------------------------------------------------
# Name:        Dictionaries.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     08.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
class_group_1 = {"Pat":12345, "Priyank":54321, "John":12345, "Mick": 766565}
class_group_2 = {"Jo":12222, "Muhammed":55555}
full_class = class_group_1 | class_group_2 # Merge new in 3.9
print (full_class)
# Example using update
full_class |= {"Xiao Xiao": 32321}
full_class |= {"Pat": 11234}
print(full_class)

print(class_group_1.get("Pat"))
class_group_2["Ciaran"]=33333
print(class_group_2)
print("Ciaran" in class_group_2) #True
name,phone=class_group_2.popitem()
print(name,phone)
print(class_group_2)
print(class_group_1.pop("John")) #removes "John":12345 and returns 12345
print(class_group_1)#{'Pat': 12345, 'Priyank': 54321, 'Mick': 766565}

staff= class_group_1.keys()
print(staff)
phones=class_group_1.values()
print(phones)
nu_list=class_group_1.items()
print(nu_list)
print(len(nu_list))