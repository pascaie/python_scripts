#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

# import the relevant modules: regex and pyperclip
import re
import pyperclip

# phone regex
phoneNumber_ro = re.compile(r'''(
                    (\d{3})         # first 3 digits
                    [-\s/]?         # separator
                    (\d{7})         # final 7 digits
                    [-\s/]?         # separator
                    ([A-Z]{2})?     # city
                    )''', re.VERBOSE)

# email regex
email_ro = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+       # username
                        @                       # at
                        [a-zA-Z0-9._]+          # domain name
                        (\.[a-zA-Z]{2,4})       # dot-something
                        )''', re.VERBOSE)

# paste text from the clipboard
text = str(pyperclip.paste())

# find all phone and email matches within the clipboard text
# definition of the list 'matches', which will contains all the matched phone numbers and emails
matches = []

    # phone number matches
for groups in phoneNumber_ro.findall(text):
    phoneNumber = '-'.join([groups[1], groups[2]])
    if groups[3] != '':
        phoneNumber += ' ' + groups[3]
    matches.append(phoneNumber)

    # email matches
for groups in email_ro.findall(text):
    matches.append(groups[0])

# copy the text to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('Neither phone numbers nor email were found')
