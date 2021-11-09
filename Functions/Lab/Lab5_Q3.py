# -------------------------------------------------------------------------------
# Name:        Lab5_Q3.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     18.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''Use the api documentation only to find out information on the necessary functions to carry out the
following tasks. Write a python script to create a menu with 3 options. Each option should call it’s own
function. Options are: 1., read in a list of LYIT Courses and a tuple of course codes 2. Edit Course names,
3. Pretty print (pprint) the data in the list., 4., for each course code check if any course name has words
in common. Print the results nicely. For example BSc in Cyber Security and M.Sc. in Cyber Security'''
import urllib
from urllib import *
from urllib.request import urlopen

link = 'https://www.lyit.ie/Study-at-LYIT/Find-a-course/'
f = urlopen(link)
myfile = f.read()
print(myfile)

menu_dictionary={1:"List of LYIT Cources",2:"Edit Course names",3:"Print the data in the list",4:"Check the words"}
list_of_cources=[]


def list_of_cources():
    print("list_of_cources")

def edit_the_cources():
    print("edit_the_cources")

def print_name_of_cources():
    print("print_name_of_cources")

def check_the_words_cources():
    print("check_the_words_cources")

def exit_the_program():
    print("{}".format("Terminating the program"))
    exit()

#list_of_functions={1: lambda: list_of_cources(),2: lambda: edit_the_cources(),3: lambda: print_name_of_cources(),4: lambda: check_the_words_cources()}

def print_main_menu():
    '''
        Function to print the menu of the menu_dictionary
        1: "List of LYIT Cources"
        2: "Edit Course names"
        3: "Print the data in the list"
        4: "Check the words"
        :return: None
    '''
    for i in (menu_dictionary.keys()):
        print("{0}: {1}".format(i,menu_dictionary.get(i)))
    return

#print_main_menu()
if __name__=='__main__':
    list_of_functions = {1: lambda: list_of_cources(), 2: lambda: edit_the_cources(),
                         3: lambda: print_name_of_cources(), 4: lambda: check_the_words_cources()}

    while True:
        print_main_menu()
        selection=input("Please choose your selection:")
        try:
            if selection.isdigit()==True and int(selection) < 5 : # checking if correct selection
                list_of_functions[int(selection)]() #calls the function from list_of_functions dictionary
            else:
                print("{}".format("You have entered wrong selection key. Try again:"))
                pass
        except:
            print("{}".format("You have entered wrong selection key. Try again:"))
            pass

