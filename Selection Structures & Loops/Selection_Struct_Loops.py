# -------------------------------------------------------------------------------
# Name:        Selection_Struct_Loops.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     08.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------


if __name__=='__main__':
    #grade = 77
    grade = input("Enter agrade: ")
    grade = int(grade)  # type cast – change the string grade to an integer and put it back in
    # the same variable!
    module1 = "python"
    # note that the operators and, or, not are valid
    if (grade >= 70) and (module1 == "python"):
        print('You have earned a Distinction!')  # Comments can be placed anywhere
        # Remember that comments should be included to explain
        # all interesting sections of code!
    elif grade >= 60:
        print("You have earned a M.1.")
    elif grade >= 50:
        print("You have earned a M.2.")
    elif grade >= 40:
        print('You have passed')
    else:
        print("Please try again")
