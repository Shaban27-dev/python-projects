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
# Number Guessing Game (computer picks random number, user guesses).
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
# Simple ATM simulator(Deposit, Withdraw, Balance).
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


#          DAY-7
# Contact Book (store name, phone, email).
def Shaban():
    info = {
        "name": "Shaban",
        "phone": "8394829812",
        "email": "alamshaban92@gmail.com",
    }
    return info

def Sarib():
    info = {
        "name": "Ssrib",
        "phone": "8394893021",
        "email": "sarib29@gmail.com",
    }
    return info

def James():
    info = {
        "name": "James",
        "phone": "9203129812",
        "email": "jamesclear40@gmail.com",
    }
    return info

def Bob():
    info = {
        "name": "Bob",
        "phone": "8399021812",
        "email": "bobshane853@gmail.com",
    }
    return info

people = {
    "shaban": Shaban,
    "sarib": Sarib,
    "james": James,
    "bob": Bob,
}

ask = input("Who do you want to know about? 'Shaban', 'Sarib', 'James', or 'Bob': ").lower()
if ask in people:
    print(people[ask]())
else:
    print("Sorry, I don't have info of that person.")


#          DAY-8
# Unit Converter (kg ↔ pounds, cm ↔ inches).
def kg_to_pounds(n1):
    return n1 * 2.2

def pounds_to_kg(n1):
    return n1 * 0.45

def cm_to_inches(n1):
    return n1 * 0.39

def inches_to_cm(n1):
    return n1 * 2.54

operations = {
    "kg_to_pounds": kg_to_pounds,
    "pounds_to_kg": pounds_to_kg,
    "cm_to_inches": cm_to_inches,
    "inches_to_cm": inches_to_cm,
}

def converter():
    print("Available conversions:")
    for symbols in operations:
        print(symbols)

    choice = input("Type the conversion you want(exactly as shown): ").lower()

    if choice not in operations:
        print("You typed an invalid conversion.")
        return
    
    value = float(input("Enter the value you want to convert: "))
    result = operations[choice](n1=value)
    print(f"Result: {result}")
    
converter()


#          DAY-9
# Bank Account OOP Project (deposit, withdraw, balance).
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
          
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Rs:", amount, "is deposited successfully.")
            print("Total balance: ", self.get_balance())
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Rs:", amount, "is withdrawn successfully.")
            print(f"Total balance: ", self.get_balance())
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance
    
acc_1 = Account(10000, 23451)

ask = input("What do you want to do? 'Deposit' or 'Withdraw': ").lower()
if ask == "deposit":
    money = int(input("How much amount do you want to deposit? "))
    acc_1.deposit(money)
elif ask == "withdraw":
    money = int(input("How much amount do you want to withdraw? "))
    acc_1.withdraw(money)
else:
    print("You typed an invalid input!")


#          DAY-10
# Quiz Game (ask 5 questions, show score).
print('''________        .__           ________                     ._.
\_____  \  __ __|__|_______  /  _____/_____    _____   ____| |
 /  / \  \|  |  \  \___   / /   \  ___\__  \  /     \_/ __ \ |
/   \_/.  \  |  /  |/    /  \    \_\  \/ __ \|  Y Y  \  ___/\|
\_____\ \_/____/|__/_____ \  \______  (____  /__|_|  /\___  >_
       \__>              \/         \/     \/      \/     \/\/''')

questions = {
    "Q1) What is the meaning of D in 'BODMAS'? ": "divide",
    "Q2) Which planet is no longer a part of our solar system? ": "pluto",
    "Q3) Who made a sacrifice of his life on 'Avengers: Endgame' movie? ": "ironman",
    "Q4) Which is the largest continent in the world? ": "asia",
    "Q5) How many countries are there in the world? ": "195",
}

score = 0

for question, correct_answer in questions.items():
    user_answer = input(question).strip().lower()

    if user_answer == correct_answer.lower():
        score += 1
        print("Correct! ✅")
    else:
        print(f"Wrong! ❌ The correct answer was {correct_answer}.")

print(f"\nYou got {score} out of {len(questions)} correct!")
print(f"Your total score is: {score}/{len(questions)} 🎉")
percentage = (score / len(questions)) * 100
print(f"You got {percentage:.2f}% correct answers out of 100%.")


#          DAY-11
# Library Management System (add/remove books, check availability).
book_list = [
    {"title": "Harry Potter", "author": "J.K. Rowling"},
    {"title": "Atomic Habits", "author": "James Clear"},
    {"title": "The Lord of the Rings", "author": "J.R.R."},
    {"title": "Lord of the Flies", "author": "William Golding"},
    {"title": "A Tale of Two Cities", "author": "Charles Dickens"},
]

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    new_book = {"title": title, "author": author}
    book_list.append(new_book)
    print(f"Book '{title}' added successfully!")

def remove_book():
    title = input("Enter book title to remove: ").strip()
    for book in book_list:
        if book["title"].lower() == title.lower():
            book_list.remove(book) 
            print(f"Book '{title}' removed successfully ❌")
            break
    else:
        print(f"Book '{title}' not found in the library!")

def check_availability():
    title = input("Enter book title to check: ").strip()
    for book in book_list:
        if book["title"].lower() == title.lower():
            print(f"'{title}' is available in the library 📚")
            break
    else:
        print(f"Book '{title}' is not available in the library ")

def view_books():
    if not book_list:
        print("No books in the library yet!")
        return
    print("Books in Library:")
    for book in book_list:
        print(f"{book['title']} — {book['author']}")

game = False

while not game:
    print("---- Library Management System ----")
    options = ["1. Add Book", "2. Remove Book", "3. Check Availability", "4. View Books", "5. Exit",]
    for el in options:
        print(el)


    ask = input("\nEnter your choice: ")
    if ask == "1":
        add_book()
    elif ask == "2":
        print("Before: ", book_list)
        remove_book()
        print("After: ", book_list)
    elif ask == "3":
        check_availability()
    elif ask == "4":
        view_books()
    elif ask == "5":
        print("Goodbye! 👋")
        game = True
    else:
        print("Please make a valid choice from the available options!")


#          DAY-12
# Student Report Card Generator (read from file, calculate average).
import os

filename = "C:\\Users\\Lenovo\\classroom\\apna college\\100days\\students.csv"

file_content = """Name,Math,Science,English,History
Shaban,91,80,88,83
Sarib,88,79,83,90
James,84,90,93,80
Ethan,90,87,81,80
Harry,85,81,78,79"""

with open(filename, "w")as f:
    f.write(file_content)

print(f"{filename} created successfully!")

def calculate_average(average):
    if average >= 90: return 'A'
    elif average >= 80: return 'B'
    elif average >= 70: return 'C'
    elif average >= 60: return 'D'
    else: return 'F'

def generate_report(file_path):
    print("-" * 65)
    print(f"{'STUDENT NAME':<15} | {'SCORE':<20} | {'AVG':<6} | {'GRADE':<3}")
    print("-" * 65)

    class_total = 0
    student_count = 0

    try:
        with open(filename, "r")as f:
            header = next(f)

            for line in f:
                parts = line.strip().split(',')

                name = parts[0]
                score = [int(value) for value in parts[1:]]
                avg = sum(score) / len(score)

                grade = calculate_average(average=avg)

                class_total += avg
                student_count += 1

                scores_str = ", ".join(map(str, score))
                print(f"{name:<15} | {scores_str:<20} | {avg:<6.1f} | {grade:<3}")

        print("-" * 65)

        if student_count > 0:
            class_avg = class_total / student_count
            print(f"Student count: {student_count}")
            print(f"Class average: {class_avg:.2f}")

    except FileNotFoundError:
        print(f"Error: The file path '{filename}' is not found!")
    except ValueError:
        print("Error: The file contains non numeric content in score columns.")

generate_report(filename)