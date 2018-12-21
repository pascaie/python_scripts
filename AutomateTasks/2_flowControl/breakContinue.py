# "break" and "continue" keyword usage within a loop

while True:  # the loop is kept alive until the if-password condition is met (the "break" will terminate the cycle)
    print('Who are you?')
    name = input()
    if name not in ('enrico', 'Enrico'):
        continue  # if name is not correct, it returns at the top of the while loop
    print('Hello Enrico! Please, enter your password: ')
    password = input()
    if password == 'swordfish':
        break  # if the password is correct, the loop is terminated
print('Access granted')
