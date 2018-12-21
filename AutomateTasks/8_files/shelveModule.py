# shelve module

import shelve

    # create a shelve file (which will correspond to 3 distinct files within the current directory)
    # store data in the shelve file using shelfFile['key'] = 'value'
    # it is commented to not to create again and again the shelve file
# shelfFile = shelve.open('.\\mydata')  # open the shelve file (it creates a new file if it does not exist)
# dogsAndCats = ['Yoda', 'Yuki', 'Iside']
# shelfFile['pets'] = dogsAndCats  # assignement of the pet list to the 'pets' key
# shelfFile.close()  # close the shelfFile

shelfFile = shelve.open('.\\mydata')
print(type(shelfFile))  # print the tyoe of the shelve file
print(shelfFile['pets'])  # print the value of the 'pets' key
shelfFile.close()

shelfFile = shelve.open('.\\mydata')
listOfKeys = list(shelfFile.keys())  # get the list of the shleve file keys
listOfValues = list(shelfFile.values())  # get the list of the shelve file values
shelfFile.close()
print(listOfKeys)
print(listOfValues)
