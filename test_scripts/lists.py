#methods for lists
# str: the list becomes a printable string
# len: returns the list's length (integer)
# append: append the newly specified element to the list
# list(<tuple>): can change a tuple into a list
# tuple(<list>): can convert a list into a tuple

#define and print list elements
mylist = ["Pam", 2, 3, "Tom"]
print(mylist[0] + ", " + mylist[3])

#the method str(<list>) transform a list into a printable string
print(str(mylist))
#the method len(<list>) returns the number of elements of the list
print(len(mylist))
#add a new element to a list using the "append" method
mylist.append("Jack")
print(len(mylist))

#list of lists
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3, 4, 5]
l3 = ['abc', 'def']
listlist = [l1, l2, l3]
print(listlist[2][1])

#TUPLES: they are like lists, but the are for "read-only", meaning that they cannot be changed
tup = ("lightspeed", "299792 km/s") #tuples are defined using round instead of box brackets
print(tup[1])
tup = ('north', 'south') #tuples can be changed only "all-at-once"
print(str(tup))

#transform a tuple into a list using "list" and change one of its element
mytuple = ('Bob', 'Rob', 'Alice')
print("original tuple: " + str(mytuple)) #with the print method, all the arguments must be of the same dtatype
#for this reason, if I print(mytuple), it will work since I only have a tuple as the print argument
#if I print("some string" + mytuple), it gives an error since I am adding a string and a tuple (which are two different dtatypes)
mylist = list(mytuple)
mylist[1] = 'Jack'
print("updated list: " + str(mylist))

#transform a list into a tuple using "tuple"
updated_tuple = tuple(mylist)
print("updated_tuple: " + str(updated_tuple))
