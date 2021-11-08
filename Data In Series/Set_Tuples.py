# -------------------------------------------------------------------------------
# Name:        Set_Tuples.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     08.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
Letters_lst=["ab","cd","aa", "db", "cd", "zx", "ws", "mn", "aa"]
b=set(Letters_lst) #this will remove the repeating items in the new collection
print(b) # {'db', 'aa', 'cd', 'ab'}
b.remove('ab')
print(b)
print(b.pop())
print(b)
b.union("a")
print(b)

tuple_a=("A")
print(type(tuple_a))
tuple_a=("A",)
print(type(tuple_a))
print(tuple_a.count("A"))

