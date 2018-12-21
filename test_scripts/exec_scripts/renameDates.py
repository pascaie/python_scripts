#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import re
import os
import shutil

# regex to find US dateformat
USDateFormat_ro = re.compile(r"""^(.*?)  # all text before the date
                            ((0|1)?\d)  # month (1 or 2 digits)
                            -?          # dash (optional)
                            ((0|1|2|3)?\d)  # day (1 or 2 digits)
                            -?          # dash (optional)
                            ((19|20)\d\d)   # year
                            (.*?)$      # all text after the date
                            """, re.VERBOSE)

workingPath = r'C:\Users\pascaie\Documents\python_test_private\test_scripts\exec_scripts\renameDates_files'
# call os.listdir() and loop through all files in the directory
for USFileName in os.listdir(workingPath):
    # check if the element of os.listdir() si a directory
    if os.path.isdir(os.path.join(workingPath, USFileName)) == True:
        # print('This is a directory: ' + USFileName)
        continue  # if it is a directory, then exit from the loop

    # use the regex to check if the filename has an US date within
    USDateFormat_mo = USDateFormat_ro.search(USFileName)

    # if the US dateformat is not found for the current USFileName, then it pass to the next step of the loop
    if USDateFormat_mo is None:
        print('No files with the American dateformat')
        continue

    # identify groups in regex
    beforePart = USDateFormat_mo.group(1)
    month = USDateFormat_mo.group(2)
    day = USDateFormat_mo.group(4)
    year = USDateFormat_mo.group(6)
    afterPart = USDateFormat_mo.group(8)

    # build the file name with the EU date format by inverting month and day
    EUFileName = beforePart + day + '-' + month + '-' + year + afterPart

    # build the absolute path of the US and EU dateformat files
    # NOTE: the EU dateformat files do not exist yet
    USFilePath = os.path.join(workingPath, USFileName)
    EUFilePath = os.path.join(workingPath, EUFileName)

    # print the renaming operations you are going to perform
    print('%s\trenamed to\t%s' % (USFileName, EUFileName))
    # use shutil.move(source, target) to rename the files by moving them within the same folder
    shutil.move(USFilePath, EUFilePath)
