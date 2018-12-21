# pprint module to save data

import pprint

pets =  [{'name': 'Yoda', 'color': 'brown', 'type': 'dog'},\
        {'name': 'Yuki', 'color': 'white', 'type': 'dog'},\
        {'name': 'Iside', 'color': 'white', 'type': 'cat'}]
# pprint.pprint(pets)  # example of pprint when printing dictionaries
pets_string = pprint.pformat(pets)  # the variable 'pets' is saved as a string

pyScript = open('.\\myPets.py', 'w')
pyScript.write('pets = ' + pets_string + '\n')  # the variable 'pets' is written into the myPets.py file
pyScript.close()
