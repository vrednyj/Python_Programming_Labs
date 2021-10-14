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
names_of_the_books=['Harry Potter','Blown Away','Anna Karenina','1984','A Christmas Carol']
price_of_the_books=[12.34, 56.32, 5.15, 6.70, 12.89]

# The wey to enter the Book title and the book price
total_cost=0
for i in range(5): # 5 iteration = 5 books to enter
    book_title=input("Please enter a book title:")
    book_cost= input("Please enter price of the book:")
    total_cost=float(total_cost)+float(book_cost)# Summing the price on each iteration
    print("{} Book price : {} Running total: {}".format(book_title,book_cost,total_cost))

# Another way
i = 0 # assigning var and value for the counter we are going to use
total_price = 0 # declaring the var and initial value
for book in names_of_the_books: # Read the names of the books from the names_of_the_books List
    total_price=price_of_the_books[i]+ total_price# getting the price for each book from price_of_the_books list and summing on each iteration
    print("Book name:{0:<20s} {1:>s} {2:5.2f} euros {3:>10s} {4:5.2f} euros".format(book,"Book price:", price_of_the_books[i],"Total:",total_price))
    i+=1 #counter