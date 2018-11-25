#dictionaries: unordered collections of key-value pairs
#they use KEYS to point VALUES
#methods:
    # <dictionary_name>[<key>] = <value> #add a key-value pair to the dictionary
    # update({<new key-value pair>})
    # pop(<key_value>) #deletes the key-value pair and returns the value

numbers = {'one': 'uno', 'two': 'due'}
print(numbers)
numbers[3] = 'tre' #add the element '3': 'tre' to the dictionary
numbers[True] = 'quattro'
print(numbers)

#retrieve a dictionary's VALUE
print(numbers['one'])

#retrieve a dictionary's LIST OF KEYS
print(numbers.keys())

#check on key existence: "<key>" in <dictionary_name>
print('one' in numbers) #True expected
print('uno' in numbers) #False expected

#dictionary length
print(len(numbers))

#update method
numbers.update({'five': 'cinque'})
print(numbers)
numbers.update({'six': 'sei', 'seven': 'sette'})
print(numbers)

#delete an element form the dictionary (you can assign it to a variable)
deleted_value = numbers.pop(3)
print(deleted_value)
deleted_value = numbers.pop('two')
print(deleted_value)

#example of useful dictionary
personal_data = {'name': 'Enrico', 'age': 26, 'weight': 80}
print(personal_data)
personal_data.pop('weight')
personal_data.update({'height': 1.80})
print(personal_data)
