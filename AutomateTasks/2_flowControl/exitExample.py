import sys

while True:
    print('Tipe \"exit\" to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
