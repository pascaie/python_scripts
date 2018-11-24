#functions

#test function
def say_hi():
    print('hi!')

say_hi()

#function with an input parameter
def say_hi(name):
    print('hi ' + name + '!')

say_hi('Jack')

#function which returns a value
def to_fahrenheit(celsius):
    f = celsius * 9/5 +32
    return f

degree_C = to_fahrenheit(20)
print('there are ' + str(degree_C) + '°F right now!')

#another conversion function: from km to mi
def to_miles(km):
    miles = km / 1.609
    return miles

distance = 100 #km
distance_mi = to_miles(distance)
print(str(distance) + ' km equals to ' + str(distance_mi) + ' mi')

#function which returns a list
def encode(numbers):
    ns = [] #create an empty list, which will be populated in the for cycle
    for n in numbers:
        ns.append(n * n)
    return ns #return the list

list1 = [1, 2, 3, 4, 5]
list2 = encode(list1)
print(list2)

#factorial function: a function nested in itself
def factorial(n):
    if n == 1:
        return 1
    else:
        return(n * factorial(n-1))

num = factorial(5)
print(num)

#function which returns a list of char belonging to the input string
def to_char(string):
    char_list = []
    for c in string:
        char_list.append(c)
    return char_list

characters = to_char('ciao, mi chaimo Enrico')
print(characters)



