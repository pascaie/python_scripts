#list of string methods present in this file:
# str: transform a datatype into a string
# len: gives the length of a string (returns an integer)
# type: returns the datatype of the argument
# replace: replace a specified substring with another (specified) one

#printing strings and integer: you have to cast the integer using the "str" method
string = "Scene "
number = 24
print(string + str(number))

#repeat a string using "*"
print("hello "*3)

#string legth: "len" method
sentence = "my name is Enrico Pascai, and I am 26 years old"
print(len(sentence))

#display the datatype: the "type" method
nationality = "" #it's an empty string
age = 26
print("nationality is of type " + str(type(nationality)) + "; age is of type " + str(type(age)))
print("nationality is a string of length "+ str(len(nationality)))

#access a string's character
name = "Captain America"
first_char = name[0]
print(first_char)
#accessing a substring
substring = name[0:7] #here, 0 index is taken (right index), while 7 (left index) is not considered
print(substring)

#"replace" method
question = "what is your name?"
question = question.replace("name", "task for today")
print(question)

#escape characters for strings --> remember: there is no difference when using " or ' for defining strings
string = 'What\'s your name?\nmy name is Enrico' #\n is the newline character
print(string)
#for long strings you can use triple quotes (i.e. """string""")
long_string = """what do you mean by saying that?
in Bologna we have a lot of different kind of pasta, but for sure \
we do not eat spaghetti alla bolognese"""
print(long_string) #triple quotes allow to newline without using \n; if you want to keep the text into the same line, just use \

#raw strings: add an r before the string definition, so that \n will ot be considered as a newline command
windows_path = r"C:\notes" #in general, in a nìstandard string, the backslash must be escaped
print(windows_path)

#string test
q = 'what\'s the speed of \
sound?'
subs = q[-6:-1]
print(subs)
q = q.replace(subs, "velociraptor")
print(q)
