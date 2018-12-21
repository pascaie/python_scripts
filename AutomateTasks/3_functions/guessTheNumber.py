# guess the number game

import random

secretNumber = random.randint(1, 20)  # randomly choose a secret number to guess

for guessTaken in range(1, 7):
    guess = int(input('Guess the number: '))  # allow you to take a new guess
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break  # break the loop if the secretNumber is guessed

if guess == secretNumber:
    print('You got it! You won!')  # 'you won' message
else:
    print('Sorry, you finished your attempts. The secret number was ' + str(secretNumber))  # 'you lost' message
