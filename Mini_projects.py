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


#          DAY-13
# Write a program for a Student Management System (OOP)
# Add student
# Remove student
# Update student marks
# Print details
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks    
    
    def update_marks(self, new_marks):
        self.marks = new_marks

    def __str__(self):
        return f"Roll No : {self.roll_no} | Name: {self.name} | Marks: {self.marks}"
        

students = []

while True:
    print("\n---- Student Management System ----")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student Marks")
    print("4. View Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = int(input("Enter roll number: "))
        marks = int(input("Enter marks: "))

        for s in students:
            if s.roll_no == roll_no:
                print("Student with this roll number already exists!")
                break
        else:
            student = Student(name, roll_no, marks)
            students.append(student)
            print("Student added successfully!")

    elif choice == "2":
        roll_no = int(input("Enter roll number to remove: "))
        for s in students:
            if s.roll_no == roll_no:
                students.remove(s)
                print("Student removed successfully!")
                break
        else:
            print("Student not found!")

    elif choice == "3":
        roll_no = int(input("Enter roll number to update marks: "))
        for s in students:
            if s.roll_no == roll_no:
                new_marks = int(input("Enter new marks: "))
                s.update_marks(new_marks)
                print("Marks updated successfully!")
                break
        else:
            print("Student not found!")

    elif choice == "4":
        if not students:
            print("No student found!")
        else:
            print("\nStudent List: ")
            for s in students:
                print(s)

    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Please make a valid choice.")


#          DAY-14
# MCQ Quiz App
# Questions stored in a list/dict
# Score tracking
# Replay option
import random
questions = [
  {
    "question": "Which planet is known as the Red Planet?",
    "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Venus"},
    "answer": "B"
  },
  {
    "question": "What is the capital of France?",
    "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
    "answer": "C"
  },
  {
    "question": "Which data type is immutable in Python?",
    "options": {"A": "List", "B": "Dictionary", "C": "Tuple", "D": "Set"},
    "answer": "C"
  },
  {
    "question": "Who wrote 'Hamlet'?",
    "options": {"A": "Charles Dickens", "B": "William Shakespeare", "C": "Leo Tolstoy", "D": "Mark Twain"},
    "answer": "B"
  },
  {
    "question": "Which gas do humans need to survive?",
    "options": {"A": "Carbon Dioxide", "B": "Oxygen", "C": "Nitrogen", "D": "Hydrogen"},
    "answer": "B"
  },
  {
    "question": "What is the largest mammal on Earth?",
    "options": {"A": "Elephant", "B": "Blue Whale", "C": "Giraffe", "D": "Hippopotamus"},
    "answer": "B"
  },
  {
    "question": "Which keyword is used to define a function in Python?",
    "options": {"A": "func", "B": "def", "C": "function", "D": "lambda"},
    "answer": "B"
  },
  {
    "question": "Which continent is the Sahara Desert located in?",
    "options": {"A": "Asia", "B": "Africa", "C": "Australia", "D": "South America"},
    "answer": "B"
  },
  {
    "question": "What is the chemical symbol for water?",
    "options": {"A": "O2", "B": "H2O", "C": "CO2", "D": "HO"},
    "answer": "B"
  },
  {
    "question": "Which year did World War II end?",
    "options": {"A": "1940", "B": "1945", "C": "1950", "D": "1939"},
    "answer": "B"
  }
]
random.shuffle(questions)

class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_no < len(self.question_list)
        
    def next_question(self):
        q = self.question_list[self.question_no]
        print(f"\nQ{self.question_no + 1}: {q['question']}")

        for key, value in q["options"].items():
            print(f"   {key}. {value}")

        while True:
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            if user_answer in q["options"]:
                break
            else:
                print("Invalid choice. please enter A, B, C and D.")

        if user_answer == q["answer"]:
            print("Correct! ✅")
            self.score += 1
        else:
            print("Wrong! ❌")

        print(f"Correct answer: {q['answer']}")
        print(f"Score: {self.score}/{self.question_no + 1}")
        
        self.question_no += 1
    
    def reset(self):
        self.question_no = 0
        self.score = 0
            

quiz = QuizBrain(q_list=questions)

while True:
    while quiz.still_has_question():
        quiz.next_question()

    percentage = (quiz.score / len(quiz.question_list)) * 100
    print("\nQuiz Completed!")
    print(f"Final Score: {quiz.score}/{len(questions)}")
    print(f"Percentage: {percentage:.2f}%")

    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again == "y":
        random.shuffle(questions)
        quiz.reset()
    else:
        print("Thanks for playing! 👋")
        break


#          DAY-15
# Simple Drawing App using Turtle
import turtle
import random

# ---------------- Screen Setup ----------------
screen = turtle.Screen()
screen.title("Simple Drawing App 🎨🐢")
screen.bgcolor("white")
screen.colormode(255)

# ---------------- Turtle Setup ----------------
tim = turtle.Turtle()
tim.speed(0)
tim.shape("turtle")
tim.pensize(3)
tim.color("black")

pen_is_down = True


# ---------------- Helper Functions ----------------
def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def turn_left():
    tim.left(15)

def turn_right():
    tim.right(15)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def reset_position():
    tim.penup()
    tim.home()
    if pen_is_down:
        tim.pendown()

def pen_up():
    global pen_is_down
    tim.penup()
    pen_is_down = False
    print("Pen is UP ✋ (not drawing)")

def pen_down():
    global pen_is_down
    tim.pendown()
    pen_is_down = True
    print("Pen is DOWN ✍️ (drawing)")

def change_color_red():
    tim.color("red")

def change_color_green():
    tim.color("green")

def change_color_blue():
    tim.color("blue")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)

def increase_brush():
    current_size = tim.pensize()
    tim.pensize(current_size + 1)
    print("Brush size:", tim.pensize())

def decrease_brush():
    current_size = tim.pensize()
    if current_size > 1:
        tim.pensize(current_size - 1)
    print("Brush size:", tim.pensize())


# ---------------- Key Bindings ----------------
screen.listen()

# Movement
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# Pen control
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "p")

# Colors
screen.onkey(change_color_red, "r")
screen.onkey(change_color_green, "g")
screen.onkey(change_color_blue, "b")
screen.onkey(random_color, "x")

# Brush size
screen.onkey(increase_brush, "+")
screen.onkey(decrease_brush, "-")

# Clear / reset
screen.onkey(clear_screen, "c")
screen.onkey(reset_position, "space")

print("🎨 Drawing App Controls:")
print("Arrow Keys: Move/Turn")
print("u = pen up | p = pen down")
print("r/g/b = colors | x = random color")
print("+ / - = brush size")
print("c = clear | space = reset position")

screen.exitonclick()
screen.mainloop()


#          DAY-16
# Smart Calculator
# Operations stored in a dictionary
# User chooses operation dynamically
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return None
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def modulo(n1, n2):
    return n1 % n2

def floor_division(n1, n2):
    if n2 == 0:
        return None
    return n1 // n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "%": modulo,
    "//": floor_division
}


def calculator():
    num1 = float(input("Enter first number: "))

    while True:
        print("Choose an operation:", " ".join(operations.keys()))
        operator = input("Operation: ").strip()

        if operator not in operations:
            print("You typed an invalid operator! Try again.\n")
            continue

        num2 = float(input("Enter second number: "))

        result = operations[operator](num1, num2)

        if result is None:
            print("❌ Error: Division by 0 is not allowed.\n")
            continue

        print(f"{num1} {operator} {num2} = {result}")

        print("\n1) Continue with current result")
        print("2) Start new")
        print("3) Exit")

        choose = input("Make a choice: ").strip()

        if choose == "1":
            num1 = result
        elif choose == "2":
            return  # exit and start again from outside
        elif choose == "3":
            print("Thanks for using calculator! 👋")
            exit()
        else:
            print("Invalid choice, exiting.")
            break


while True:
    calculator()


#          DAY-17
#Modify Snake Game:
# Change speed
# Change colors
# Add pause feature
from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.colormode(255)

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

segments = []

for position in STARTING_POSITION:
    new_piece = Turtle("square")
    new_piece.color("white")
    new_piece.penup()
    new_piece.goto(position)
    segments.append(new_piece)

head = segments[0]

# ---------------- Movement Controls ----------------
def up():
    if head.heading() != DOWN:
        head.setheading(UP)

def down():
    if head.heading() != UP:
        head.setheading(DOWN)

def left():
    if head.heading() != RIGHT:
        head.setheading(LEFT)

def right():
    if head.heading() != LEFT:
        head.setheading(RIGHT)

# ---------------- Color Controls ----------------
def snake_color_red():
    for seg in segments:
        seg.color("red")

def snake_color_green():
    for seg in segments:
        seg.color("green")

def snake_color_blue():
    for seg in segments:
        seg.color("blue")

def snake_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    for seg in segments:
        seg.color(r, g, b)

def background_color_black():
    screen.bgcolor("black")

def background_color_navy():
    screen.bgcolor("navy")

def background_color_yellow():
    screen.bgcolor("yellow")

# ---------------- Speed + Pause ----------------
delay = 0.1
paused = False

def speed_up():
    global delay
    if delay > 0.02:
        delay -= 0.01

def speed_down():
    global delay
    delay += 0.01

def toggle_pause():
    global paused
    paused = not paused

# ---------------- Snake Movement ----------------
def move():
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(MOVE_DISTANCE)

# ---------------- Key Bindings ----------------
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.onkey(snake_color_red, "r")
screen.onkey(snake_color_green, "g")
screen.onkey(snake_color_blue, "b")
screen.onkey(snake_random_color, "x")

screen.onkey(background_color_black, "1")
screen.onkey(background_color_navy, "2")
screen.onkey(background_color_yellow, "3")

screen.onkey(speed_up, "+")
screen.onkey(speed_down, "-")
screen.onkey(toggle_pause, "p")

# ---------------- Game Loop ----------------
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(delay)

    if not paused:
        move()

        # Wall collision check
        if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
            print("GAME OVER! You hit the wall.")
            game_is_on = False

screen.exitonclick()


#          DAY-18
#Mini Game Framework
# Base Game class
# Child classes for different games
import random


# ---------------- Base Framework ----------------
class Game:
    def __init__(self):
        self.score = 0

    def start_menu(self):
        print("\n---- Welcome to Mini Games ----")
        print("1. Guess the Number")
        print("2. Quiz Game")
        print("3. Rock Paper Scissors")
        print("4. Exit")

    def end_game(self):
        print("\nGame Over!")
        print(f"Your score: {self.score}")

    def play_game(self):
        raise NotImplementedError("Child class must implement play_game()")


# ---------------- Game 1: Guess the Number ----------------
class GuessTheNumber(Game):
    def __init__(self):
        super().__init__()

    def play_game(self):
        print("\nStarting Guess the Number Game!")
        computer_choice = random.randint(0, 20)

        while True:
            try:
                guess = int(input("Make a guess between 0 and 20: "))
            except ValueError:
                print("Please enter a valid number between 0 and 20.")
                continue

            if guess < 0 or guess > 20:
                print("Out of range! Please choose between 0 and 20.")
                continue

            if guess < computer_choice:
                print("Too low!")
            elif guess > computer_choice:
                print("Too high!")
            else:
                print("Correct! 🎉")
                self.score += 1
                break

        self.end_game()


# ---------------- QuizBrain Helper Class ----------------
class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        q = self.question_list[self.question_no]
        print(f"\nQ{self.question_no + 1}: {q['question']}")

        for key, value in q["options"].items():
            print(f"   {key}. {value}")

        while True:
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            if user_answer in q["options"]:
                break
            print("Invalid choice. Please enter A, B, C, or D.")

        if user_answer == q["answer"]:
            print("Correct! ✅")
            self.score += 1
        else:
            print("Wrong! ❌")

        print(f"Correct answer: {q['answer']}")
        print(f"Score: {self.score}/{self.question_no + 1}")

        self.question_no += 1


# ---------------- Game 2: Quiz Game ----------------
class QuizGame(Game):
    def __init__(self):
        super().__init__()

    def play_game(self):
        print("\nStarting Quiz Game!")

        questions = [
            {
                "question": "Which planet is known as the Red Planet?",
                "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Venus"},
                "answer": "B"
            },
            {
                "question": "What is the capital of France?",
                "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
                "answer": "C"
            },
            {
                "question": "Which data type is immutable in Python?",
                "options": {"A": "List", "B": "Dictionary", "C": "Tuple", "D": "Set"},
                "answer": "C"
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "options": {"A": "Charles Dickens", "B": "William Shakespeare", "C": "Leo Tolstoy", "D": "Mark Twain"},
                "answer": "B"
            },
            {
                "question": "Which gas do humans need to survive?",
                "options": {"A": "Carbon Dioxide", "B": "Oxygen", "C": "Nitrogen", "D": "Hydrogen"},
                "answer": "B"
            },
            {
                "question": "What is the largest mammal on Earth?",
                "options": {"A": "Elephant", "B": "Blue Whale", "C": "Giraffe", "D": "Hippopotamus"},
                "answer": "B"
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": {"A": "func", "B": "def", "C": "function", "D": "lambda"},
                "answer": "B"
            },
            {
                "question": "Which continent is the Sahara Desert located in?",
                "options": {"A": "Asia", "B": "Africa", "C": "Australia", "D": "South America"},
                "answer": "B"
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": {"A": "O2", "B": "H2O", "C": "CO2", "D": "HO"},
                "answer": "B"
            },
            {
                "question": "Which year did World War II end?",
                "options": {"A": "1940", "B": "1945", "C": "1950", "D": "1939"},
                "answer": "B"
            }
        ]

        new_questions = random.sample(questions, 5)
        quiz = QuizBrain(q_list=new_questions)

        while quiz.still_has_question():
            quiz.next_question()

        percentage = (quiz.score / len(new_questions)) * 100
        print("\nQuiz Completed!")
        print(f"Final Score: {quiz.score}/{len(new_questions)}")
        print(f"Percentage: {percentage:.2f}%")

        self.score += quiz.score
        self.end_game()


# ---------------- Game 3: Rock Paper Scissors ----------------
class RockPaperScissors(Game):
    def __init__(self):
        super().__init__()

    def play_game(self):
        print("\nStarting Rock Paper and Scissors Game!")

        choices = ["rock", "paper", "scissors"]
        user_score = {"wins": 0, "lose": 0, "draws": 0}
        round_no = 1

        while True:
            print(f"\n_____ Round {round_no} _____")
            user_choice = input("Pick one (rock/paper/scissors): ").lower().strip()

            if user_choice not in choices:
                print("Invalid input. Please type rock, paper, or scissors.")
                continue

            computer_choice = random.choice(choices)
            print(f"Computer choice: {computer_choice}")

            if user_choice == computer_choice:
                print("It's a draw!")
                user_score["draws"] += 1

            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                print("You Win! ✅")
                user_score["wins"] += 1
                self.score += 1
            else:
                print("You lose! ❌")
                user_score["lose"] += 1

            print(f"Scoreboard: wins={user_score['wins']} | loses={user_score['lose']} | draws={user_score['draws']}")
            round_no += 1

            if user_score["wins"] == 5:
                print("You are the champion! 🏆")
                break
            elif user_score["lose"] == 5:
                print("Computer is the champion! 😢")
                break

        self.end_game()


# ---------------- Launcher ----------------
launcher = Game()

while True:
    launcher.start_menu()
    choice = input("Choose a game (1-4): ").strip()

    if choice == "1":
        GuessTheNumber().play_game()
    elif choice == "2":
        QuizGame().play_game()
    elif choice == "3":
        RockPaperScissors().play_game()
    elif choice == "4":
        print("Thanks for playing. Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.")