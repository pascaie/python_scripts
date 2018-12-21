# usage of os.walk(folder_path)

import os

folderPath = r'C:\Users\pascaie\Documents\python_test_private\test_scripts\exec_scripts\renameDates_files'

for folderName, subFolderNames, fileNames in os.walk(folderPath):
    print('The current folder is: ' + folderName)
    for subFolderName in subFolderNames:
        print('Its subFolders are: ' + subFolderName)
    for fileName in fileNames:
        print('Which contains the files: ' + fileName)
    print('')
