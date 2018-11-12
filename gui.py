path_to_jsons = r'I:\jsondata'
import os
import json
from easygui import *

# def main():
#     potential_files = os.listdir(path_to_jsons)
#     no_json_file_names = [i.split('.')[0] for i in potential_files]
#     print(no_json_file_names)
#
#
#     base_json = {
#      "staffTypes": staffTypes_dict,
#      "revenueGoal": rev_goal,
#      "shiftStart": start_string,                                                             ### should have this export to the correct user
#      "shiftEnd": end_string                                                                  ### should have this export to the correct user
# }                                                                                            ### should have this export to the correct user
#     with open(json_name, 'wb'):                                                              ### should have this export to the correct user
#         json.dump(base_json)                                                                 ### should have this export to the correct user
#



if __name__ == '__main__':
    msg = "Enter your personal information"
    title = "fox optimization something or another"
    fieldNames = ["Username","Password"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames)

    print('here')
    from profile_managemnet import username_and_passwords
    auth = username_and_passwords()

    while 1:
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])

        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
        result = auth.check_login(fieldValues[0],fieldValues[1])
        if result == False:
            msgbox('Username or password was incorrect','Auth Error')
            continue
        if result == True:
            if errmsg == "":
                break # no problems found
