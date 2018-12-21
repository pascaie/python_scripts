#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os
import zipfile

# source folder: it contains the files to be backed up
folderPath = r'C:\Users\pascaie\Documents\python_test_private\test_scripts\exec_scripts\quizFiles'
# target folder: where the .zip files are stored
folderBkpPath = r'C:\Users\pascaie\Documents\python_test_private\test_scripts\exec_scripts\bkp'

# change the current directory to the source folder
os.chdir(folderPath)

number = 1  # initialization of the backup file number (N)

while True:
    zipFileName = 'quizFilesBackup_' + str(number) + '.zip'  # definition of the zip file name: quizFilesBackup__N.zip
    if os.path.exists(os.path.join(folderBkpPath, zipFileName)):
        number += 1  # if the file already exists, then increase the number N and make another cycle
    else:
        break  # if the Nth file does not exists, exit from the cycle

newZipFile = zipfile.ZipFile(os.path.join(folderBkpPath, zipFileName), 'w')  # create the Nth .zip file

# usage of the os.walk method to find all the files contained within the source folder
# NOTE that the source folder is also the current folder (i.e. '.')
for folderName, subFolderNames, fileNames in os.walk('.'):  # walk all the subfolders and files within the current folder
    print('Folder: ' + folderName)  # print the folder name (increasing the cycle, this same folder may represent the current folder's subfolders)
    for fileName in fileNames:  # cycle through all the files contained within the 'folderName' folder
        print('File: ' + fileName)  # print the file name (this file is going to be backed up)
        # compress the file using the .write method ---> the compressed file is inserted in a tree hierarchy correspondent to the one of the source folder
        newZipFile.write(os.path.join(folderName, fileName), compress_type=zipfile.ZIP_DEFLATED)  # this is the command which effectively compress the files
    print('')  # leave a space in the file list visualization whenever a folder is changed to a subfolder

newZipFile.close()  # close the ZipFile object
