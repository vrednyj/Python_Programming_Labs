# -------------------------------------------------------------------------------
# Name:        Lab2_Q3.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     09.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------

'''Given the variable suffix_no with a value of 1122. Build an LYIT student number. The number should
begin with an L and be followed by 8 digits. Where the suffix_no is less than 8 the string should be
padded with zero’s to a final size of 8. Use only string methods and variables to carry out this task. Do
not use loops or selection structures. Modify your answer to take in the suffix_no from the user.
'''

suffix_no=1122
print('L{:08d}'.format(suffix_no))

suffix_no=input("Please enter your student number:")
print('L{:08d}'.format(int(suffix_no))) #converting string from the input inot int
#or
print('L{:0>8s}'.format(suffix_no))# not converting string. Enother method.