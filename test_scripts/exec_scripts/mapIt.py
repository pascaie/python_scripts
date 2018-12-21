#! python3
# mapIt.py - open Google Maps in the web browser with the specified address

import webbrowser
import sys
import pyperclip

# two ways of taking the input:
# 1) from the command line, as the arguments after the mapIt command
# 2) from the clipboard
# NOTE that (1) has the priority with respect to (2)

if len(sys.argv) > 1:
    # get the address from the command line
    address = ' '.join(sys.argv[1:])
else:
    # get the address from the clipboard
    address = pyperclip.paste()


webbrowser.open('https://www.google.it/maps/place/' + address)
