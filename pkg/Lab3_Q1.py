# -------------------------------------------------------------------------------
# Name:        Lab3_Q1.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     09.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''Create a guessing game. Allow the user to input a number. Test to see if their guess is right. If it is
wrong then ask if they want to guess again. Repeat until they either get the answer the right number
or until they say no when asked if they wish to retry'''
import random

random_number=random.randint(1,10) #generates random number between 1 and 10
input_message="Please guess the number between 1 and 10 or press \"q\" to exit:"
#print(random_number) # for debug

number_of_guess=0
while 1:
    user_guess=input(input_message)
    print("You have entered: {}".format(user_guess))
    number_of_guess+=1

    if user_guess.isdigit()==True and int(user_guess)!=random_number:# checks if the entered value is digit
        re_try=input("Bad guess, do you want to try again? Yes(Y)/No(N)")
        if re_try.isdigit()==False and re_try.lower()=="n":
            break
        else:
            pass

    elif user_guess.lower()=="q" :
        print("{0} {1}. Exiting the game.".format("The number to guess was",random_number))
        break

    elif user_guess.isdigit()!=True :
        print("{0}".format("Wrong key selection."))

    else:
        print("{0} {1}. It took you {2} iterations to guess the number.".format("Good guess!!! The number is",random_number,number_of_guess))
        break