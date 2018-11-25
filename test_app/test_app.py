word = 'arzigogolato'
wordSpell = list(word)
print(wordSpell)

wordLength = len(wordSpell)
rightList = list('_' * wordLength)

finished = False
while finished == False:
    guess = input('Guess a letter: ')

    if guess not in word:
        print('This letter is not in the word')

    for letter in wordSpell:
        if letter == guess:
            index = wordSpell.index(guess)
            rightList[index] = guess
            wordSpell[index] = '_'

    print(rightList)

    if list(word) == rightList:
        finished = True
        print('You win!')
