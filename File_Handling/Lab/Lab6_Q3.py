# -------------------------------------------------------------------------------
# Name:        Lab6_Q3.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     25.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
'''When performing data analytics data often has to be processed from multiple files simultaneously.
Navigate through a folder and save the name of each text or doc file into a list so that the data can be
read at a later date'''

import os

list_of_files_for_analisys=[]

def practice_q (dir_for_search):
    """
    Practice Question for File Handling
    :return:
    """
    size = 0
    total_size = 0
    print("Please wait while the folders scanning is in progress...")
    if os.path.exists(dir_for_search):
        for folder_name, sub_folder, file_names in os.walk(dir_for_search):
            for file_name in file_names:
                size = os.path.getsize(os.path.join(folder_name, file_name))
                #print(file_name)
                if file_name.endswith(".txt") or file_name.endswith(".doc"):
                    list_of_files_for_analisys.append(os.path.join(folder_name, file_name))
                else:
                    pass
            total_size = total_size + size
        print("The contents of this directory is: {} bytes".format(total_size))
    else:
        pass


if __name__=='__main__':
    dir_for_search=input("Please enter the directory for search:")
    practice_q(dir_for_search)

    if list_of_files_for_analisys == []:
        print("No files with txt or doc extensions found is the current directory.")
    else:
        report_file=open("report_file.log", "w")
        for i in list_of_files_for_analisys:
            report_file.write(i+"\n")
        #print(list_of_files_for_analisys)
        report_file.close()
        print("Please check {} file to see reports".format(report_file.name))