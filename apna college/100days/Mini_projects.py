#          DAY_1
# Write a program to make a simple calculator(take two numbers + operator, print result).
"""a = int(input("Enter first num: "))
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
    print("Invalid input!")"""

# Treasure game using tkinter (copilot)
"""import tkinter as tk
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

root.mainloop()"""


#          DAY_2
# Write a program for Password Strength Checker (if length < 8 → weak, else strong).
"""password = input("Enter password: ")

if len(password) >= 8:
    print("Strong password!")
else:
    print("Weak password!")"""

#          DAY_3
# Write a code for number guessing game (computer picks random number, user guesses)
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
