# -------------------------------------------------------------------------------
# Name:        test.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     04.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
def func(n):
    print(n)
    if(n==1):
        print(n)
        return 1;
    else:
        print(n)
        return(n+func(n-1))
print(func(4))

n =(m for m in range(3))
for m in n:
   print(m)
for m in n:
   print(m)