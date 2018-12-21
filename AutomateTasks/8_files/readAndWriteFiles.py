# reading and writing files

import os

currentPath = os.getcwd()  # C:\Users\pascaie\Documents\python_test_private\AutomateTasks\8_files

newTXTFile = open('.\\newFile.txt', 'r')  # already exixting text file where I wrote 'ciao'
content = newTXTFile.read()  # reads the file content
print(content)  # print the file content

newTXTFile_write = open('.\\newFile_write.txt', 'w')  # create a new file in 'write' mode
newTXTFile_write.write('Hello, my name is Enrico\n')  # write to file
newTXTFile_write.close()  # closes the file

newTXTFile_write = open('.\\newFile_write.txt', 'a')  # open the file in 'append' mode
newTXTFile_write.write('I am 26 years old')  # append the text to the opened file
newTXTFile_write.close()

newTXTFile_write = open('.\\newFile_write.txt', 'r')  # open the file in 'read' mode
content_string = newTXTFile_write.read()
newTXTFile_write.close()
print(content_string)  # print the read content of the file

newTXTFile_write = open('.\\newFile_write.txt', 'r')
# readlines() method reads the file content and returns a list of strings, one string for each line of the file
content_listOfStrings = newTXTFile_write.readlines()
newTXTFile_write.close()
print(content_listOfStrings)
