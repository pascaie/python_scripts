# pictures location: C:\Users\pascaie\Pictures

import os  # work with files and the Operating System
from datetime import datetime

folder = r"C:\Users\pascaie\Pictures\pictures_download"  # "r" is for "raw string"
location = input("Photo location: ")  # asks the user to input a location which will be added to the new filename
files = os.listdir(folder)  # creates a list of the elements within the folder

for filename in files:
    if not filename.startswith('.'):  # do not consider the "."-named files/directories
        file = os.path.join(folder, filename)  # joins the folder with the file
        extension = os.path.splitext(file)  # split the file and its extension, i.e. returns a 2-element list
        # print(extension)

        m_time = os.path.getmtime(file)  # get the last modification time
        # print(m_time) # this returns the seconds passed since January 1st, 1970
        real_time = datetime.fromtimestamp(m_time)  # get the last modification time in a readable format
        # print(real_time)

        f_time = datetime.strftime(real_time, "%Y%m%d_%H%M%S")  # here you can edit the output format of the date
        # print(f_time)

        new_filename = location + "_" + f_time + extension[1]  # compose the new new_filename
        # OBS: express the extension as the second element of the extension variable
        new_file = os.path.join(folder, new_filename)  # get the path and name of the new file

        os.rename(file, new_file)  # here, the files are effectively renamed with the new names
