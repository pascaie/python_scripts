#LOOPS

#while loop
#runs until the condition is TRUE
var = True
while var == True:
    print("echo")
    var = False

#counter variable in a while loop (it stops the loop)
number = 0
while number < 3:
    print(number)
    number = number + 1

#for loop
for num in range(1,4):
    print(num)

#for loop used to cycle on array elements
names = ["Snap", "Crackle", "Pop"]
for name in names:
    print(name)
