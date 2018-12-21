# definition of a global variable within a function (local space)
# the newly globally defined variable will override any existing global variable having the same name

def spam():
    global eggs
    eggs = 10

eggs = 1
spam()
print(eggs)  #the printed output is: 10
