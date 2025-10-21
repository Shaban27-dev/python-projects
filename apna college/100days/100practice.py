# Q1)  We're going to build a tip calculator.
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay:
# 150.00 / 5) * 1.12 = 33.6
# After formatting the result to 2 decimal places = 33.60
"""print("welcome to tip calculator!")

bill = float(input("what was the total bill? :"))
tip = int(input("what percentage tip would you like to give? 10 12 15 :"))
people = int(input("how many people to split the bill? :"))

split = int(bill * ((tip/100) + 1) / people)
print("your total bill is :", split)"""


# Q2)  WAP TO CALCULATE THE FINAL PRIZE OF A PIZZA.
#  Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1
"""print("welcome to pizza deliveries!")
size = input("what size pizza do you want? S, M OR L :")
pepporoni = input("do you want pepporoni on your pizza? Y or N :")
extra_cheese = input("do you want some extra cheese on your pizza? Y or N :")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong input")

if pepporoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print("Your total bill is :", bill)"""
 

# Q3)  Write a Python program that asks the user for their height in centimeters and determines if they can ride a rollercoaster.
# If the height is 120 cm or more, ask for their age and calculate the ticket price as follows:
# Age < 12: ticket is $5
# Age 12–18: ticket is $7
# Age between 45–55 (inclusive): ticket is free
# All other ages: ticket is $12
# Then ask if they want a photo taken (Y or N). If they say "Y", add $3 to the bill.
# Finally, print the total bill.
# If the height is less than 120 cm, print a message saying they can’t ride.
"""print("Hello!, Welcome to the rollercoaster")
height = int(input("What is your height in cm :"))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age :"))
    
    if age < 12:
        bill = 5
        print("Kids tickets are for 5$.")
    elif age > 12 and age < 18:
        bill = 7
        print("Youths tickets are for 12$.")
    elif age > 45 and age < 55:
        bill = 0
        print("Your tickets are free.")
    else:
        bill = 12
        print("Your tickets are for 12$.")
else:
    print("You have to grow taller in order to ride the rollercoaster!.")"""


# Q4)  1. First Choice: Ask the user to choose a direction at a crossroads:
# If they type "left" → proceed
# If they type "right" → print "You fell into a hole. Game Over." and end the game.

# 2. Second Choice: If they chose left, they reach a lake. Ask if they want to "wait" for a boat or "swim" across:
# If "swim" → print "You got drowned. Game Over." and end the game.
# If "wait" → proceed to next stage.

# 3. Third Choice: The player now sees 3 doors: "red", "yellow", and "blue". Ask which door they choose:
# "yellow" → print "YOU WON!"
# Any other color → print "You opened the wrong door. Game Over."

# print(r
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
# |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# )

"""print("Welcome to the treasure island!")
print("Your mission is to find the treasure!")

choice_1 = input("you are in a turning, where do you want to go? type 'left' or 'right' ").lower()
if choice_1 == "right":
    choice_2 = input("you came infront of a boat, what do you want to do? 'sit' or 'walk around' ").lower()
    if choice_2 == "sit":
        choice_3 = input("There are three doors infront of you, which one do you want to open? 'red', 'green' or 'yellow' ").lower()
        if choice_3 == "red":
            print("You found the treasure, CONGRATULATION!")
        elif choice_3 == "green":
            print("you got bitten by a snake, GAME OVER!")
        else:
            print("You got attacked by a lion, GAME OVER!")
    else:
        print("An Elephant killed you, GAME OVER!")
else:
    print("you fell into a hole, GAME OVER!")"""

# Q5)  Create a coin flip program using what you have learnt about randomisation in Python. 
# It should randomly print "Heads" or "Tails" everytime it is run.
"""import random
toss = random.randint(0, 1)
if toss == 0:
    print("HEADS")
else:
    print("TAILS")

toss = random.randint(0, 5)
if 0 < toss < 5:
    print("TAILS")
else:
    print("HEADS")"""

# Q6)  Figure out how to pick a random name from the list of friends.
"""import random
names = ["shaban", "sarib", "arsil", "taush", "sharukh"]

print(random.choice(names))"""

# Q7)  ROCK, PAPER AND SCISSORS WITH COMPUTER.
#      0 FOR ROCK, 1 FOR PAPER AND 2 FOR SCISSORS.
"""rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''"""

"""import random
game_images = [rock, paper, scissors]
user_choice = int(input("What do you want to choose? 0 for Rock, 1 for Paper and 2 for Scissors :"))

if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number, You lose!")
else:
    computer_choice = random.randint(0, 2)

    print("\nyou choose :")
    print(game_images[user_choice])
    print("computer_choose :")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0:
        if computer_choice == 2:
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == 2:
        if computer_choice == 1:
            print("You win!")
        else:
            print("You lose!")"""


# Q8)  PRINT THE MAXIMUM AND MINIMUM SCORES FROM A STUDENTS_SCORES LIST WITHOUT USING MAX() AND MIN() FUNCTION.
"""student_scores = [199, 109, 155, 187, 180, 28, 83, 74, 99]

max_num = student_scores[0]
for el in student_scores:
    if el > max_num:
        max_num = el
print(max_num)

min_num = student_scores[0]
for item in student_scores:
    if item < min_num:
        min_num = item
print(min_num) 

sum = 0
for a in student_scores:
    sum += a
print(sum)"""

# Q9)  WAP TO PRINT RANDOM PASSWORD GENERATOR WHICH ALSO ASKS THE USER FOR HOW MANY LETTERS, NUMBERS AND SYMBOLS.
"""import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to random password generator!")
nr_letter = int(input("How many letters would you like to have in your password?\n"))
nr_numbers = int(input("How many numbers would you like to have in your password?\n"))
nr_symbols = int(input("How many symbols would you like to have in your password?\n"))

password_list = []
for char in range(0, nr_letter):
    password_list.append(random.choice(letters))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = "".join(password_list)
print(password)"""



# WORD GUESSING GAME
"""import random
from itertools import combinations_with_replacement
from random import vonmisesvariate

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        print("You win.") """

"""youngest = {}

while True:
    name = input("enter your name: ")
    age = int(input("Enter your age: "))
    youngest[name] = age
    add = input("Type 'yes' to add more person else 'no': ").lower()
    print("\n" * 10)
    if add == "no":
        break

least_age = min(youngest, key=youngest.get)
print(f"The youngest person is {least_age} with age = {youngest[least_age]}") """

"""n = int(input("Enter a num: "))

if n % 2 == 0 and 2 <= n <= 5:
    print("what")
else:
    print("No") """

#Odd or Even Game!
"""import random

def odd_even_game():
    n = int(input("Enter a number (1-100): "))
    computer_choice = random.randint(1, 100)
    print(f"Computer chose: {computer_choice}") 

    if n % 2 == computer_choice % 2:
        print("You guessed right! You win!")
    else:
        print("Wrong guess! You lose.")

while True:
    game = input("Do you want to play ODD/EVEN GAME? (y/n): ").lower()
    if game != "y":
        print("Goodbye!")
        break

    odd_even_game()

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break"""


# NUMBER GUESSING GAME.
"""import random

def num_guessing(attempt, max_num):
    computer_choice = random.randint(1, max_num)
    while attempt > 0:
        try:
            user_choice = int(input(f"Guess a num between 1 and {max_num}: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if user_choice < computer_choice:
            print("Your guess is too low!")
            print(f"Hint: Try between {user_choice + 1} and {max_num}")
        elif user_choice > computer_choice:
            print("Your guess is too high!")
            print(f"Hint: Try between {1} and {user_choice - 1}")
        else:
            print("You guessed it right!")
            score = attempt * 10
            print("Your score is:", score)
            return
        
        if abs(user_choice - computer_choice) <= 3:
            print("You're very close!")
        elif abs(user_choice - computer_choice) <= 7:
            print("You're close!")

        attempt -= 1
        print(f"attempts left {attempt}")
    
    print(f"You ran out of attempts. computer_choice was {computer_choice}")
    return 0

best_score = 0

while True:
    difficulty_level = input("Choose difficulty level, 'Easy', 'Medium', or 'Hard': ").lower()
    if difficulty_level == "easy":
        attempt = 10
        max_num = 50
    elif difficulty_level == "medium":
        attempt = 5
        max_num = 75
    else:
        attempt = 3
        max_num = 100

    score = num_guessing(attempt, max_num)
    if score is not None:
        if score > best_score:
            best_score = score
            print("New High score!")

    print(f"Best score so far {best_score}/n")


    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break """


# ROCK PAPER SCISSORS GAME.
"""import random

choice = ["rock", "paper", "scissors"]

user_score = {"wins": 0, "lose": 0, "draws": 0}

round_number = 1

def game():
    global round_number
    print(f"_____Round-Number-{round_number}_____") 
    user_choice = input("Pick one, 'rock', 'paper', or 'scissors': ").lower()

    if user_choice not in choice:
        print("Please enter a valid input!")
        return
    
    computer_choice = random.choice(choice)
    print(f"computer_choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
        user_score ["draws"] += 1

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper") :
        print("You win!")
        user_score ["wins"] += 1
    else:
        print("You lose!")
        user_score ["lose"] += 1

    round_number += 1
        
        
should_continue = True
while should_continue:
    game()

    print(f"\nUser's_Scoreboard: wins = {user_score['wins']} | loses = {user_score['lose']} | draws = {user_score['draws']}" )

    if user_score["wins"] == 5:
        print("You are the champion!")
        break
    elif user_score["lose"] == 5:
        print("Computer is the champion!")
        break

    play_again = input("Do you want to play again?(Y/N): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        should_continue = False  """


# QUIZ GAME
"""def quiz_game():
    while True:
        score = 0
        ask = input("Do you want to play QUIZ GAME? (Y/N): ").lower()
        if ask == "y":
            question_1 = input("What is the capital of India?" 
            " [a) Mumbai  b) kolkata c) Delhi d) Bangolore] = ").lower()
            if question_1 == "delhi":
                score += 10
                print(f"current score is {score}")
                question_2 = input("which country is known as heaven?" \
                " [a) Iceland  b) switzerland c) New zealand d) Australia] = ").lower()
                if question_2 == "iceland":
                    score += 10
                    print(f"current score is {score}")
                    question_3 = input("which planet is closest to Earth?" \
                    " [a) Mars  b) Venus c) Saturn d) Jupitor] = ").lower()
                    if question_3 == "venus":
                        score += 10
                        print(f"Final score is {score}")
                        print(f"Your all answers were correct. Your total score is {score}")
                        break
                    else:
                        print("Your answer is wrong, the correct answer is 'Venus'!")
                        break
                else:
                    print("It's wrong, correct answer is 'Iceland'!")
                    break
            else:
                print("Wrong answer, Delhi is the right answer!")
                break
        else:
            print("Have a nice day!")

quiz_game()"""


"""def quiz_game():
    questions = [
         {
        "question": "What is the capital of India?",
        "options" : ["a) Mumbai, b) kolkata, c) Delhi, d) Bangolore"],
        "answer" : "c"
    },
    {
        "question": "which country is known as heaven?",
        "options": ["a) Iceland, b) switzerland, c) New zealand, d) Australia"],
        "answer": "a"
    },
{
        "question": "which planet is closest to Earth?",
        "options": ["a) saturn, b) venus, c) mercury, d) jupitor"],
        "answer": "b"
}
    
]
    
    score = 0

    while True:
        ask = input("Do you want to play QUIZ_GAME? (Y/N): ")
        if ask != "y":
            print("Have a nice day!")
            break

        for q in questions:
            print("\n" + q["question"])
            for option in q["options"]:
                print(option)

            answer = input("Your answer: ").lower()
            if answer == q["answer"]:
                score += 10
                print(f"Correct!, your current score {score}")
            else:
                print(f"Wrong!, correct answer was {answer}")
                
        print(f"\nFinal score {score}")

        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != "y":
            print("Thanks for playing")
            break    
    

quiz_game()"""


# NUMBER GUESSING GAME:
"""import random

def num_guess(attempt, max_num):
    computer_choice = random.randint(0, max_num)
    while attempt > 0:
        try:
            user_choice = int(input(f"Guess a number between 0 and {max_num}: "))
        except ValueError:
            print(f"please make a guess between 0 and {max_num}")
            continue

        if user_choice < computer_choice:
            print("Your guess is too low!")
            print(f"Hint: Make a guess between {user_choice + 1} and {max_num}")
        elif user_choice > computer_choice:
            print("Your guess is too high!")
            print(f"Hint: Make a guess between {0} and {user_choice - 1}")
        else:
            attempt -= 1
            print("Your guess is correct!")
            score = attempt * 10
            print(f"You guessed it in {attempt} attempt")
            return score
            break
        
        if abs(user_choice - computer_choice) <= 3:
            print("You are very close!")
        elif abs(user_choice - computer_choice) <= 7:
            print("You are close!")

        attempt -= 1
        print(f"attempts left {attempt}")

        if attempt == 0:
            print(f"you ran out of attempts, computer choice was {computer_choice}")
            return 0


best_score = 0

while True:
    difficulty_level = input("How much difficulty do you want? 'Easy', 'Medium' or 'Hard': ").lower()
    if difficulty_level == "easy":
        attempt = 10
        max_num = 50
    elif difficulty_level == "hard":
        attempt = 5
        max_num = 75
    else:
        attempt = 3
        max_num = 100
    
    score = num_guess(attempt, max_num)
    if score is not None:
        if score > best_score:
            best_score = score
            print("New High Score!")

    print(f"Best score so far {best_score}\n")


    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again != "y":
        print("Thanks for playing.")
        break"""


# ROCK PAPER SCISSORS GAME
"""import random

choices = ["rock", "paper", "scissors"]

def game():
    user_score = {"wins": 0, "loses": 0, "draws": 0}
    round_number = 1

    while True:
        print(f"\n_____ Round {round_number} _____")
        computer_choice = random.choice(choices)
        user_choice = input("Choose 'rock', 'paper' or 'scissors': ").lower()

        if user_choice not in choices:
            print("❌ Invalid choice. Please select rock, paper, or scissors.")
            continue

        if user_choice == computer_choice:
            user_score["draws"] += 1
            print(f"🤝 Both chose {user_choice}. It's a draw!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            user_score["wins"] += 1
            print(f"✅ You win! {user_choice} beats {computer_choice}")
            print(f"You need {5 - user_score['wins']} more wins to become the champ!")
        else:
            user_score["loses"] += 1
            print(f"❌ You lose! {computer_choice} beats {user_choice}")
            print(f"If you lose {5 - user_score['loses']} more rounds, you’ll be a loser!")

        print(f"📊 Current Score: {user_score}")
        round_number += 1

        # Check win/lose condition
        if user_score["wins"] == 5:
            print("\n🎉 You won 5 rounds! You are the CHAMPION! 🏆")
            break
        elif user_score["loses"] == 5:
            print("\n😢 You lost 5 rounds! Better luck next time!")
            break

    return user_score


# Main loop
while True:
    final_score = game()
    print(f"\nFinal Scoreboard: {final_score}")

    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again != "y":
        print("👋 Thanks for playing Rock-Paper-Scissors!")
        break"""


# RANDOM PASSWORD GENERATOR
"""import random
import string

def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    no_of_letters = int(input("how many letters do you want in your password? "))
    no_of_numbers = int(input("how many numbers do you want in your password? "))
    no_of_symbols = int(input("how many symbols do you want in your password? "))

    password_list = []

    for char in range(0, no_of_letters):
        password_list.append(random.choice(letters))
    for char in range(0, no_of_numbers):
        password_list.append(random.choice(numbers))
    for char in range(0, no_of_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"your random generated password is: {password}")  

while True:
    generate_password()
    again = input("Do you want to generate a random password again? (Y/N): ").lower() 
    if again != "y":
        print("Goodbye!")
        break """


# MY OWN PROJECT
"""import random 
import string

def game():
    letters = string.ascii_lowercase
    computer_choice = random.choice(letters)
    attempt = 10

    while attempt > 0:
        guess = input("Guess a letter: ").lower()

        if guess == computer_choice:
            print("Congratulations!, You guessed it right!")
            return
        else:
            attempt -= 1
            print("Wrong!, Try again.")
            print(f"attempts left:{attempt}")

should_continue = True
while should_continue:
    game()
    play_again = input("Do you want to play agian? (Y/N): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        should_continue = False"""


# CALCULATOR
"""def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error, can't be divisible by 0"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error, modulo by 0 is not allowed!"
    return a % b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
}

answers = []
def calculator():
    num1 = float(input("Enter first num: "))
    while True:
        for symbol in operations:
            print(symbol)
        choose = input("pick an operator: ")
        num2 = float(input("Enter second num: "))

        if choose in operations: 
            result = operations[choose](num1, num2)
            print(f"{num1} {choose} {num2} = {result}")
        else:
            print("You typed an invalid input!")
            break

        answers.append(result)

        choice = input(f"Type 'Y' to continue calculating with {result} or 'N' with new number. For quitting the game type 'Q': ").lower()
        if choice == "y":
            num1 = result
        elif choice == "n":
            return calculator()
        else:
            print("Thanks for using calculator. Goodbye!")
            print(f"answers so far {answers}")
            break

calculator()"""


# NUMBER GUESSING GAME
import random

def num_guessing(attempt, max_num):
    computer_choice = random.randint(1, max_num)

    while attempt > 0:
        user_input = input(f"Make a guess between 1 and {max_num} or 'q' to quit: ").lower()

        if user_input == "q":
            print("You quit the game!")
            return None

        try:
            user_choice = int(user_input)   # only convert if it's not 'q'
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")
            continue


        if user_choice < 1 or user_choice > max_num:
            print(f"Your guess must be between 1 and {max_num}")
            continue

        if user_choice < computer_choice:
            print("Too low")
            print(f"Hint: Try between {user_choice + 1} and {max_num}")
        elif user_choice > computer_choice:
            print("too high")
            print(f"Hint: Try between 1 and {user_choice - 1}")
        else:
            print("You guessed it right!")
            score = attempt * 10 
            print(f"Your score: {score}")
            return score

        diff = abs(user_choice - computer_choice)
        if diff <= 3:
            print("You're very close!")
        elif diff <= 5:
            print("You're close!")

        attempt -= 1
        print(f"attempts left: {attempt}")

    print(f"You ran out of attempt!. computer_choice was {computer_choice}")
    return 0


best_score = 0

while True:
    difficulty_level = input("Choose difficulty level. 'Easy', 'Medium' or 'Hard': ").lower()
    if difficulty_level == "easy":
        attempt, max_num = 10, 50
    elif difficulty_level == "medium":
        attempt, max_num = 5, 75
    else:
        attempt, max_num = 3, 100

    score = num_guessing(attempt, max_num)
    
    if score is not None:
        if score > best_score:
            best_score = score
            print(f"New High score: {best_score}")

    play_again = input("Do you want to play again? Type (Y/N): ").lower()
    if play_again != "y":
        print(f"Thanks for playing! Your best score is {best_score}") 
        break