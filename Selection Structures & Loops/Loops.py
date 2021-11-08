# -------------------------------------------------------------------------------
# Name:        Loops.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     08.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------


if __name__=='__main__':

# for loops
    for i in range(5, 10):
     print(i)
    #Simplified Bizz, Buzz game
    for i in range(1, 10):
        if i == 5:
             print("Buzz")
             print("bizz")
    print("\n")
    #Stop when you find a 6
    #break statement stops the loop
    for i in range(1, 10):
        if i == 6:
         print("Found")
         break
    print("Not Yet")
    print("It was found at {}".format(i))  #iterate over letters
    from string import ascii_lowercase
    for ch in ascii_lowercase:
        print(ch)

# While loops

    max=5
    counter=0
    total=0
    while counter <= max :
         total+=9.99
         counter+=1
    print("The final amount is: {0:5.2f}".format(total))

    #While true sample
    text=""
    while 1:
         print ("Enter name")
         uname=input()
         if(uname == "joe"):
            break
    print("Finished")


