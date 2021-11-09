# -------------------------------------------------------------------------------
# Name:        Jason_exmp.py
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
Parsing a Json file
"""
import json
def parse_student_json_data(file_name):
     """
     :param file_name:
     :return:
     """
     fh = open(file_name)
     for line in fh:
          raw_data = json.loads(line)
          print("{}".format(raw_data['first_name']))

def parse_provisioner_json_data(file_name):
    """
    :param file_name:
    :return:
    """
    # fh = open(file_name)
    # raw_data = json.loads(fh)

    with open(file_name, "r") as read_file:
         data = json.load(read_file)
         #print(json.dumps(data, indent=4, sort_keys=True)) #Sorting
         #print(json.dumps(data, indent=4, sort_keys=False))  # dumps ->printing
         #print(type(data)) # object comes in as a dictionary
         #print(data) # contents of the dictionary are shown for clarity here
         # navigate through the dictionary items
         provisioner_details = data["members"][0]["name"] #- > Molecule Man
         print(type(data["members"])) # ->List
         print(type(data["members"][0]))  # ->Dic
         #provisioner_details = data['name']
         print("Provisioner Details: {}".format(provisioner_details)) # this is a list of dictionaries
         print("\n\nItems in Provisioner List:")

         for item in provisioner_details:
             print(item, "\n") # iterate through the dictionaries in the list of configuration items

if __name__ == "__main__":
     # parse_student_json_data("jsons_prov.jason")
     parse_provisioner_json_data("jsons_prov.json")
     new_data = {"student_id": "L000223344", "first_name": "Jo",
     "last_name": "Michaels"}
     print(new_data)
     with open("jsons", "a") as write_file:
          write_file.write('\n') # move onto a newline before writing object
          json.dump(new_data, write_file, indent=4,)
