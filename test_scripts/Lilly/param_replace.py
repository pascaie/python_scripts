#! python3

# parameter replacer (using regex)

import re
import pyperclip

# list of the parameters which are present in the source file
listOfParam = ['<table_1>',
                '<table_2>',
                '<id_1>',
                '<id_2>',
                '<id_value_1>',
                '<id_value_2>',
                '<join_key_1>',
                '<join_key_2>']

# list of the values that you want to substitute to each parameter
# note that the values have to be listed in the same order with respect to the parameter list
listOfVal = ['PROJECT_LIST',
            'PROJECT_TASK',
            'PROJECT_ID',
            'TASK_ID',
            '1234',
            '59567',
            'PROJECT_ID(PRJ)',
            'PROJECT_ID(TSK)']

# display an error message if the length of the two lists is different
if len(listOfParam) != len(listOfVal):
    raise Exception('The lists of parameters and its respective list of values must have the same length')

# read the .txt document and save it as a string
TXTFile = open(r'C:\Users\pascaie\Documents\python_test_private\test_scripts\Lilly\sample_file.txt', 'r')  # open the .txt file
text = TXTFile.read()  # reads the file content

# for-cycle though all elements of the listOfParam
for i in range(len(listOfParam)):
    # regex definition
    substitute_ro = re.compile(listOfParam[i])
    # substitution
    text = substitute_ro.sub(listOfVal[i], text)

# copy to clipboard
pyperclip.copy(text)
