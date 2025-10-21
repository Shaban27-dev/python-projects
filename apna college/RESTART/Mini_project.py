#          GUESS THE NUMBER
"""import random

target = random.randint(1, 100)

while True:
    userChoice = (input("Guess the target or Quit(Q) : "))
    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Guess < target")
    else:
        print("Guess > target")

print("----GAME OVER----")"""

#          RANDOM PASSWORD GENERATOR
"""import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [function for i in range(n)]

password = "".join([random.choice(charValues) for i in range(pass_len)])

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)

print("your random password is : ", password)""" 

# Q1)  COUNT NO OF EVEN AND ODD NUMBERS BETWEEN 1 TO 100.
"""even_count = 0
odd_count = 0

for num in range(0, 100):
    if num % 2 == 0:
        even_count += 1
else:
        odd_count += 1

print("total even number :", even_count)
print("total odd number :", odd_count)"""

# Q2)  RANDOM GUESSING GAME.
"""import random
num = random.randint(0, 10)
game = False
tries = 0

while not game:
    guess = int(input("Make a guess (0-10):"))
    tries += 1
    if guess == num:
         print(f"correct!, You guessed it in {tries} tries")
         game = True
    elif guess < num:
        print("your guess is too low!")
    else:
        print("your guess is too high")"""
     
# Q3)  Ask the user for a word, then print only the vowels in that word using a loop and conditionals.
"""word = input("Write a word :").lower()
vowels = "aeiou"
vowel_letters = ""

for letter in word:
    if letter in vowels:
        vowel_letters += letter

print(vowel_letters)"""

# Q4)  CREATE A FUNCTION FOR FRIENDSHIP CALCULATOR SCORE.
"""def friendship_calculator(name1, name2):
    set1 = set(name1)
    set2 = set(name2)

    set3 = set1.intersection(set2)
    print("common words are :",set3)

friendship_calculator("shaban", "sarib")"""

# Q5)  CREATE FUNCTION WHICH COUNTS THE NO OF VOWELS OF YOU AND YOUR PET'S NAME.    
"""def count_vowels(owner, pet):
    vowels = "aeiou"
    vowel_count = 0

    combine_names = (owner + pet)

    for letter in combine_names:
        if letter in vowels:
            vowel_count += 1

    print("vowel count is :", vowel_count)
count_vowels("raj", "shiro") """