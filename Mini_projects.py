#          DAY_1
# Simple Calculator(take two numbers + operator, print result).
a = int(input("Enter first num: "))
c = input("Choose one from these('+', '-', '*', '/'): ")
b = int(input("Enter second num: "))

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error: Division by 0!")
else:
    print("Invalid input!") 

# Treasure Game using tkinter (copilot). This code is not written by me.
import tkinter as tk
from tkinter import messagebox

def start_game():
    label.config(text="You are at a crossover. Where do you want to go?")
    button_left.config(text="LEFT", command=fall_in_hole)
    button_right.config(text="RIGHT", command=ocean_scene)
    button_left.pack()
    button_right.pack()

def fall_in_hole():
    messagebox.showinfo("Game Over", "You fell into a hole!")

def ocean_scene():
    label.config(text="You are in front of an ocean. What do you want to do?")
    button_left.config(text="SWIM", command=trout_attack)
    button_right.config(text="WAIT", command=door_scene)

def trout_attack():
    messagebox.showinfo("Game Over", "You got attacked by trout!")

def door_scene():
    label.config(text="There are three doors. Which one will you open?")
    button_left.config(text="RED", command=burned)
    button_middle.config(text="YELLOW", command=win_game)
    button_right.config(text="BLUE", command=eaten_by_beasts)
    button_middle.pack()
    button_left.pack()
    button_right.pack()

def burned():
    messagebox.showinfo("Game Over", "Wrong door! You got burned!")

def eaten_by_beasts():
    messagebox.showinfo("Game Over", "Wrong door! You got eaten by beasts!")

def win_game():
    messagebox.showinfo("Victory", "You got the treasure! You win!")

# GUI setup
root = tk.Tk()
root.title("Treasure Island")
root.geometry("500x300")

label = tk.Label(root, text="Welcome to Treasure Island!", font=("Helvetica", 14))
label.pack(pady=20)

button_left = tk.Button(root, text="", width=15)
button_middle = tk.Button(root, text="", width=15)
button_right = tk.Button(root, text="", width=15)

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

root.mainloop()


#          DAY_2
# Password Strength Checker (if length < 8 → weak, else strong).
password = input("Enter password: ")

if len(password) >= 8:
    print("Strong password!")
else:
    print("Weak password!")

#          DAY_3
# Number Guessing Game (computer picks random number, user guesses)
import random

def num_guessing(attempt, max_num):
    computer_choice = random.randint(0, max_num)
    
    while attempt > 0:
        try:
            user_choice = int(input(f"Make a guess between 0 and {max_num}: "))
        except ValueError:
            print(f"Please make a guess between 0 and {max_num}")
            continue

        if user_choice < computer_choice:
            print("Your guess is too low!")
            print(f"Hint: Make guess between {user_choice + 1} and {max_num}")
        elif user_choice > computer_choice:
            print("Your guess is too high!")
            print(f"Hint: Make a guess between 0 and {user_choice - 1}")
        else:
            attempt -= 1
            print("Your guess is correct!")
            score = attempt * 10
            print(f"you guessed it in {attempt} attempts!")
            return score
            break

        if abs(user_choice - computer_choice) <= 3:
            print("You are very close!")
        elif abs(user_choice - computer_choice) <= 5:
            print("You are close!")

        attempt -= 1
        print(f"Attempts left: {attempt}")

        if attempt == 0:
            print(f"You ran out of attempts. Computer guess was {computer_choice}")
            return 0
        
best_score = 0
worst_score = 0

while True:
    difficulty_level = input("How much difficulty do you want to go with? (Easy, Medium or Hard): ").lower()
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
            print("New high score!")
        elif score < best_score:
            worst_score = score
            print("Worst score")
    
    print(f"Best score so far {best_score}\n")
    print(f"Worst score so far {worst_score}\n")   
 
    play_again = input("Do you want to play again? (YES/NO): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break


#          DAY_4
# Simple ATM simulator(Deposit, Withdraw, Balance)
balance = 10000

def check_balance():
    print(f"Your current balance is ${balance:.2f}")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} deposited succesfully.")
    else:
        print("Invalid deposit amount")

def withdraw(amount):
    global balance
    if amount <= balance and amount > 0:
        balance -= amount
        print(f"${amount:.2f} withdrawn successfully!")
        check_balance()
    elif amount > balance:
        print("Insufficient funds!")
    else:
        print("Invalid withdrawal amount!")

def atm():
    while True:
        ask = input("what do you want to do? ('Deposit', 'Withdraw', 'check_balance' or 'exit'): ").lower()
        if ask == "exit":
            print("Thanks for using ATM, GOODBYE!")
            break
        if ask == "check_balance":
            check_balance()
        elif ask == "deposit":
            amt = float(input("How much amount do you want to deposit: "))
            deposit(amt)
        elif ask == "withdraw":
            amt = float(input("How much amount do you want to withdraw: "))
            withdraw(amt)
        else:
            print("Invalid choice!")

atm()


#          DAY_5
# To-Do List program (add, remove, view tasks).
tasks = []

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task})
    print(f"✅ Task '{task}' added successfully!")

def remove_task():
    if len(tasks) == 0:
        print("⚠️ No tasks to remove!")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']}")

    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed_task = tasks.pop(num - 1)
            print(f"🗑️ Task '{removed_task['task']}' removed successfully.")
        else:
            print("⚠️ Please enter a valid task number!")
    except ValueError:
        print("❌ Please enter a valid number.")

def view_tasks():
    if len(tasks) == 0:
        print("📭 No tasks added yet!")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("👋 Thanks for using the To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

main()


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

choses_word = random.choice(words_list)

placeholder = ""
word_length = len(choses_word)
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
    
    for letter in choses_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("word to guess: " + display)

    if guess not in choses_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word_list. You lose a life")
        
        if lives == 0:
            game_over = True
            print(f"***************IT WAS {choses_word}! YOU LOSE***************")

    if "_" not in display:
        game_over = True
        print("***************YOU WIN!***************")

    print(stages[lives])