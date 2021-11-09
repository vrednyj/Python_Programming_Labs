# -------------------------------------------------------------------------------
# Name:        CSV_Handling.py
# Project:     Python_Programming_Labs
#
# Author:      Vitaliy Baseckas
#
# Created:     09.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
"""
Description
----------
Parsing a csv file with the csv module
"""
import csv
def parse_csv_file(file_name):
    """
    Parse sample insurance file using csv module
    :param
    file_name: insurance statistics file
    :return:
    None
    """
    fh = open(file_name)
    fr = csv.reader(fh)
    #sample_data = list(fr)#[1] #would return the file data set as a list
    sample_data=fr
    #print(sample_data)
    marion = 0
    pinellas = 0
    for row in fr:
        if fr.line_num == 1:
           continue

        if row[2] == 'MARION COUNTY':
           marion += 1

        if row[2] == 'PINELLAS COUNTY':
           pinellas += 1
    print("Marrion has {0} and Pinellas has {1} insurance policies".format(marion, pinellas))

    from collections import Counter
    c = Counter(sample_data)
    # c2 = Counter()
    print( c.items() )
if __name__ == "__main__":
     parse_csv_file('FL_insurance_sample.csv')