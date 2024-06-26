import json
import os

def load_person_data():

    cwd = os.getcwd ()
    print(cwd)
    try:
        file = open ("data/person_db.json")
    except:
        file = open ("../data/person_db.json")
    person_data = json.load(file)
    return person_data

def get_person_list(person_data):

    list_of_names = []

    for eintrag in person_data:
        list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
    return list_of_names

def get_imgae_path(person_data, person_name):

    for eintrag in person_data:
        if person_name == eintrag["lastname"] + ", " +  eintrag["firstname"]:
            return eintrag["picture_path"]
    return None



