# -------------------------------------------------------------------------------
# Name:        Lab4_Q2.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     09.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''Create a list of ten names for week 1 lotto players. Generate a list of random numbers from 1
to 20. Create a dictionary from the values. Repeat the process to create another list ten names
as per below with random lotto numbers allocated.
Week 1: Joe, John, Jane, Mick, Mary, Ann, Rick, John, Aine, Brenda
Week 2: Jack, Mary, Phil, John, Pat, Joe, Luke, Bill, Ben, Nathan
Once the data has been created:
2.1 Find the intersection in the lists to find out who bought tickets on both weeks
2.2 Create a list of the unique members who have played over the two weeks
2.3 What were the most common lotto numbers
2.4 Did any member pick the same number on multiple occasions'''
import random

List_of_names_1=["Joe","John", "Jane", "Mick", "Mary", "Ann", "Rick", "Pat", "Aine", "Brenda"]
List_of_names_2=["Jack", "Mary", "Phil", "John", "Pat", "Joe", "Luke", "Bill", "Ben", "Nathan"]
random_numbers=[] # list of random numbers for each ticket.
random_number_list=[]
#common_numbers_list=[] not used
week_1_players={}
week_2_players={}
gamblers=[]
common_number_count=0

for a in range(len(List_of_names_1)): #Assigning lottery numbers for each player for week 1
    for i in range(6): # ticket with 6 numbers in it
        random_numbers.append(random.randint(1,45)) # random numbers from 1 to 45
    random_numbers.sort()
    week_1_players[List_of_names_1[a]]=random_numbers #Assigning lottery numbers for each player in format {name:[list of random numbers]}
    random_number_list+random_numbers # will be used for statistic to find and count most common number
    random_numbers = [] #reseting lotto numbers to asign a new numbers to the next player

for a in range(len(List_of_names_2)): #Assigning lottery numbers for each player for week 2
    for i in range(6):
        random_numbers.append(random.randint(1,45)) # random numbers from 1 to 45
    random_numbers.sort()
    week_2_players[List_of_names_2[a]]=random_numbers #Assigning lottery numbers for each player in format {name:[list of random numbers]}
    random_number_list=random_number_list+random_numbers # will be used for statistic to find and count most common number week 1 and week 2
    random_numbers = [] #reseting lotto numbers to asign a new numbers to the next player

# 2.1 Find the intersection in the lists to find out who bought tickets on both weeks
#2.2 Create a list of the unique members who have played over the two weeks
for a in List_of_names_1:
    if a in List_of_names_2:# checking if name from List_of_names_1 in List_of_names_2 one by one
        print ("{} has played Lotto two weeks in a row".format(a))
        gamblers.append(a)# identifying the gamblers

#2.3 What were the most common lotto numbers
for i in range(1,46):
    number_count=random_number_list.count(i)# counting the numbers one by one in the random_number_list.
    if number_count > common_number_count: # condition if the current number count greater of previous number count
        common_number_count=number_count # if so assign that count number to common_number_count
        common_number=i # identifying the most common number

print("The number {0} is most common and has been chosen {1} times.".format(common_number,common_number_count))

#2.4 Did any member pick the same number on multiple occasions'''

for s in range(len(gamblers)): # we have already made the list of the gamblers
    for i in week_1_players[gamblers[s]]: # checking their numbers from week one and week two one by one
        if i in week_2_players[gamblers[s]]:# if the number in week 1 is in week 2 print the name and that number.
            print("{0} has selected number {1} multiple times".format(gamblers[s],i))

