#bool test
print("apples" == "oranges")
print("apples" != "oranges")

#variable assignement of bool type, plus print
sentence = True
print(sentence)

result = 1 != 10
print(result)

#usage of the "if" statement to execute commands if a condition is met
if True:
    print("the command is being executed!")

#if with conditional statement (with string)
password = "Swordfish04"
if password == "Swordfish04":
    print("Welcome, user!")

#if with conditional statement (with integer)
score = 50
if score < 100:
    print("you need more points!")

#if-else statement
newScore = 99
if newScore == 100:
    print("you made exactly 100 points")
else:
    print("your score is not 100")

#if-elif-else statement
hour = 14
if hour < 12:
    print("good morning")
elif hour < 17:
    print("good afternoon")
else:
    print("good night")
