#! env/bin/python
# Ryan Simmons
# H A N G M A N

import random
from string import ascii_lowercase


def menu():
    play = input('Type "play" to play the game, "exit" to quit: ')
    if play == 'play':
        return True
    elif play == 'exit':
        return False


def game():

    word_bank = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(word_bank)
    mercy = "-" * len(word)
    count = 0
    guessed_letters = []

    while count != 8:

        if mercy == word:   # breaks loop if user guessed word
            break
        print()
        print(mercy)
        guess = input('Input a letter: ')

# Checks user input section
        if len(guess) > 1:
            print('You should input a single letter')
        elif guess not in ascii_lowercase:
            print('It is not an ASCII lowercase letter')
        elif guess in guessed_letters:
            print('You already typed this letter')
        elif guess in word and guess not in mercy:
            for i in range(len(word)):
                if word[i] == guess:
                    mercy = list(mercy)
                    mercy[i] = guess
                    mercy = "".join(mercy)
        else:
            print('No such letter in the word')
            count += 1
        guessed_letters.append(guess)

# Game end section
    if mercy != word:
        print('You are hanged!')
        print()

    if mercy == word:
        print()
        print(mercy)
        print('You guessed the word!')
        print('You survived!')
        print()


print('H A N G M A N')
while menu():
    game()
