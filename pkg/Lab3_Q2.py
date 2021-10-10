# -------------------------------------------------------------------------------
# Name:        Lab3_Q2.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     09.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''Read in 5 book titles and values. After each title and value is read in display the values and produce a
running total of the cost
BookTitle1 Cost Running Total
Type casting may be necessary.
num_1 ="10.99"
num_2="12.99"
total=float(num_1)+float(num_2)
print (total)'''

total_cost=0
for i in range(5):
    book_title=input("Please enter a book title:")
    book_cost= input("Please enter price of the book:")
    total_cost=total_cost+float(book_cost)
    print("{} Book price : {} Running total: {}".format(book_title,book_cost,total_cost))
