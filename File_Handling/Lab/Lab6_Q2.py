# -------------------------------------------------------------------------------
# Name:        Lab6_Q2.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     25.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''Carry out the question above but navigate through the subfolders and sum up the total in the folder
and nested sub folders.'''
import os
def practice_q(dir_for_search):
    """
    Practice Question for File Handling
    :return:
    """
    size = 0
    total_size = 0
    if os.path.exists(dir_for_search):
        for folder_name, sub_folder, file_names in os.walk(dir_for_search):
            for file_name in file_names:
                size = os.path.getsize(os.path.join(folder_name, file_name))
            total_size = total_size + size
        print("The contents of this directory is: {} bytes".format(total_size))
    else:
        pass

if __name__=='__main__':
    dir_for_search=input("Please enter the directory for search:")
    practice_q(dir_for_search)
