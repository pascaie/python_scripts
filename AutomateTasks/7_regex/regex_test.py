# Python script to test regular expressions

import re

# test on the regex object's search method and match object handling (with groups)
phoneNumber_ro = re.compile(r'(\d{3})[-\s](\d{7})')
mo = phoneNumber_ro.search('My name is Enrico and my phone number is 338 9401022')
print('phone number found: ' + mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.groups())

# test on greedy and nongreedy match
    # greedy
greedyHa_re = re.compile(r'(ha){3,5}')  # greedy regex
greedyMo = greedyHa_re.search('hahahahaha')
print('greedy regex: ' + greedyMo.group())
    # nonGreedy
nonGreedyHa_re = re.compile(r'(ha){3,5}?')  # nongreedy regex
nonGreedyMo = nonGreedyHa_re.search('hahahahaha')
print('nonGreedy regex: ' + nonGreedyMo.group())

# regex object's findall method
    # groups ARE NOT DECLARED within the regex object definition
phoneNumber_roWoGroups = re.compile(r'\d{3}[-\s]\d{7}')  # without groups
numberList = phoneNumber_roWoGroups.findall('my number is 338 9401022, my mother\'s one is 338-3339811')
print(numberList)  # returns the list of all the matched strings
    # groups ARE DECLARED within the regex object definition
phoneNumber_roWGroups = re.compile(r'(\d{3})[-\s](\d{7})')  # without groups
groupList = phoneNumber_roWGroups.findall('my number is 338 9401022, my mother\'s one is 338-3339811')
print(groupList)  # returns a list of tuples, each tuple containing all groups matched

# character classes
xmas_ro = re.compile(r'\d+\s\w+')
xmasList = xmas_ro.findall('1 pc, 1 mouse, 1 keyboard, 1 Amazon gift card, 3 books')
print(xmasList)

# defining character classes
charClass_ro = re.compile(r'[aeiouAEIOU]')  # match any vowel
vowelList = charClass_ro.findall('Aiuole fiorite, con le rose')
print(vowelList)

NegativeCharClass_ro = re.compile(r'[^A-Z]')
noLetterList = NegativeCharClass_ro.findall('Ciao, mi chiamo Enrico. Ho 26 anni.')
print(noLetterList)

# using ^ and $
beginsWith_ro = re.compile(r'^\d+')  # matches the strings that begin with
print(beginsWith_ro.findall('ciao, mi chaimo Enrico'))  # this returns an empty list (i.e. [])
print(beginsWith_ro.search('ciao, mi chaimo Enrico'))  # this returns 'None' since it is a match object
print(beginsWith_ro.findall('1, 2, 3, mi chaimo Enrico'))  # returns '1'
print(beginsWith_ro.findall('11111, 22222, 33333, mi chiamo Enrico'))  # returns '11111'

onlyNumString_ro = re.compile(r'^\d+$')  # matches a string which is composed only of digits
print(onlyNumString_ro.search('123 abc'))
print(onlyNumString_ro.search('123 456789'))
print(onlyNumString_ro.search('123456789'))  # only this string returns a match

# match everything with (.*)
name_ro = re.compile(r'First Name: (.*); Last Name: (.*)')
name_mo = name_ro.search('First Name: Enrico; Last Name: Pascai')
print(name_mo.group(1))
print(name_mo.group(2))

# re.DOTALL as the second re.compile() argument ---> also the newline is matched by (.*)
newlineRegex = re.compile(r'.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# case-insensitive match
caseInsensitive_ro = re.compile(r'robocop', re.IGNORECASE)
print(caseInsensitive_ro.search('RoboCop is half man, half robot.').group())

# sub() method
substitute_ro = re.compile(r'Agent \w+')  # recognize 'Agent' and the word after it (i.e. the name of the Agent)
newString = substitute_ro.sub('CENSORED', 'Agent Watson was contacted by Agent Charlie')  # substitute the Agent <name> with 'CENSORED'
print(newString)

# sub() method with substituting in a portion of the matched string
subtituteInitial_ro = re.compile(r'Agent (\w)\w+')
newString_1 = subtituteInitial_ro.sub(r'Agent \1****', 'Agent Watson was contacted by Agent Charlie')
print(newString_1)

# manage complex regex using re.VERBOSE
complexRegex_ro = re.compile(r'''(
                    (\d{3})         # first 3 digits
                    [-\s/]?       # separator
                    (\d{7})         # final 7 digits
                    [-\s/]?       # separator
                    [A-Z]*     # city (zero or more uppercase letters)
                    )''', re.VERBOSE)
numString = '''List of telephone numbers:
                3383339811,
                338/9401022,
                051-9312910,
                3389401022 MI'''
numList = complexRegex_ro.findall(numString)
print(numList)
# print(len(numList))
for i in range(0, len(numList)):
    print(numList[i][0])

print(complexRegex_ro.search(numString).group())

# sample email list for phoneAndEmail.py test script input
#enr.pas@mail.it
# enr_p@lib.com
# rr.lo@mic.uk
