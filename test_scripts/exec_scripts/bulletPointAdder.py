#! python3

# bulletPointAdder - adds bullet points to each line of text on the clipboard

import pyperclip

text = pyperclip.paste()  # input text is taken from the clipboard

# separate the lines and add the star (*)
lines = text.split('\n')  # split the lines into an array of strings - it consider the '\n' as the array element separator
for i in range(len(lines)):  # i runs through each element of the lines array
    lines[i] = '* ' + lines[i]  # modify each lines element by adding the star
text = '\n'.join(lines)  # join the lines element in a single string, placing a '\n' between them

print(text)  # you can comment this line, it just print the script output (which is also copied to the clipboard)
pyperclip.copy(text)  # saves the output text into the clipboard

# OBS: launching the script multiple times in a row will result in adding more and more stars at the beginning of each line
