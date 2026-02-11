#          DAY-6
# Guess the Word Game(like hangman lite).
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

words_list = ["apple", "mango", "sky", "balloon", "rocket", "science", "atom", "humans", "psychology", "study", "evolution"]

import random

lives = 6

chosen_word = random.choice(words_list)

placeholder = ""
word_length = len(chosen_word)
for _ in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"***************{lives}/6 Lives left***************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You have already guessed the letter: ", guess)

    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word_list. You lose a life")
        
        if lives == 0:
            game_over = True
            print(f"***************IT WAS {chosen_word}! YOU LOSE***************")

    if "_" not in display:
        game_over = True
        print("***************YOU WIN!***************")

    print(stages[lives])