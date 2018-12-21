#! python3

# pw.py - Python script to manage the passwords related to different online accounts

import sys
import pyperclip

PASSWORDS = {'email_libero': 'LiberoMail1234!',
            'giallo_zafferano': 'Spaghetti2017!',
            'valigia': '99112'}

if len(sys.argv) < 2:
    print('Usage: pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
