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
input_message="Please guess the number between 1 and 10 or press \"q\" to exit:" # Added q key in case the user wants to quit.
#print(random_number) # for debug

number_of_guess=0
while 1:
    user_guess=input(input_message)
    print("You have entered: {}".format(user_guess)) #bring on the screen the number entered by the user
    number_of_guess+=1 #counter to count number of guesses

    # checks if the entered value is digit and it's not equal to the looking number.
    # If the entered values is not digit another scenario is in place.
    if user_guess.isdigit()==True and int(user_guess)!=random_number:
        re_try=input("Bad guess, do you want to try again? Yes(Y)/No(N)")# Gives an option to continue the game or not.
        if re_try.isdigit()==False and re_try.lower()=="n": # Eliminating the letter cases.
            break
        else:
            pass

    elif user_guess.lower()=="q" : # This will quit the game is the user presses 'q'
        print("{0} {1}. Exiting the game.".format("The number to guess was",random_number))
        # Prints out the information what was the number to guess.
        break

    elif user_guess.isdigit()!=True : # Warns the user to select right key/number
        print("{0}".format("Wrong key selection."))

    else:
        print("{0} {1}. It took you {2} iterations to guess the number.".format("Good guess!!! The number is",random_number,number_of_guess))
        #Prints out the number to guess ans the guesses iterations.
        break