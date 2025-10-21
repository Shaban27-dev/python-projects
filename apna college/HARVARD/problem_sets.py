# ---PROBLEM_SET_0---

# INDOOR VOICE
"""name = (input("enter your name: ")).lower()
print(name)"""

# PLAYBACK
"""game = input("Enter anything: ")
playback = game.replace(" ", "...")
print(playback) """

# MAKING FACES
"""# Define your emoji mapping
emoji_map = {
    ":)": "😊",   # smile
    "(:": "😢",   # sad
    ":D": "😄",   # big smile
    ":(": "☹️",   # frown
    ";)": "😉"    # wink
}

# Sample input string
text = input("enter text: ")

# Replace symbols with emojis
for symbol, emoji in emoji_map.items():
    text = text.replace(symbol, emoji)

print(text)"""

#  EINSTEIN
"""print("Einstein Theory of Relativity")
m = int(input("enter m: "))
c = 300000000
E = m * (c ** 2)
print(f"E = {E}")"""

# TIP CALCULATOR
"""bill = float(input("How much was your bill? "))
tip = int(input("How much tip do you want to give? "))
total = bill * (1 + tip/100)
rounded = round(total, 2)
print(f"Your total is {rounded}")"""


# STRING MANIPULATION PRACTICE
#1 Replace spaces with dashes
"""text = input("Enter text: ")
print(text.replace(" ", "_"))"""

#2 Count words in a sentence
"""text = input("Enter text: ")
word = text.split()
print(f"Number of words: {len(word)}")"""

#3 Capitalize each letter of first word
"""text = input("Enter text: ")
print(text.title())"""

#4 Reverse each word
"""text = input("Enter text: ")
words = text.split()
reversed_word = [word[::-1]for word in words]
print(" ".join(reversed_word))"""

#5 Remove all vowels
"""text = input("Enter text: ")
vowels = "aeiouAEIOU"
result = "".join([ch for ch in text if ch not in vowels])
print(result)"""

#6 **Customer censor (Replace bad words with **)
"""text = input("Enter text: ")
bad_words = ["bad", "ugly", "loser", "fool"]

for bad in bad_words:
    text = text.replace(bad, "*" * len(bad_words))

print(text)"""


# ---PROBLEM_SET_1---

#1 Deep Thought
"""def deep_thought():
    
    answer = input("what is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    if answer in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")
while True:
    n = deep_thought()
    play = input("Want to play again? Y?N: ").lower()
    if play != "y":
        print("Thanks")
        break"""

#2 Home Federal Savings Bank
"""def greet():
    money = 0
    ask = input("Greeting: ").title()
    if ask == "Hello":
        print(f"${money}")
    elif ask[0] == "H":
        print(f"${money + 20}")
    else:
        print(f"${money + 100}")
greet()"""

#3 File Extensions
"""def file():
    filename = input("File name: ")
    extension = filename.split('.')[-1]
    if extension in ["gif","jpg","jpeg","png","pdf","txt","zip"]:
        print(f"image/{extension}")  # Output: jpg
    else:
        print("It's not in extension!")
file()"""

#4 Math Interpreter
"""def math():
    x = int(input("Enter x: "))
    y = input("choose from ('+','-','*','/'): ")
    z = int(input("Enter z: "))
    if y == "+":
        print("Expression:", x + z)
    elif y == "-":
        print("Expression:", x - z)
    elif y == "*":
        print("Expression:", x * z)
    elif y == "/":
        if z == 0:
            print("can't be divided by 0")
        else:
            print("Expression:", x / z)
    else:
        print("Invalid input!")
math()"""

#5 Meal Time
"""from datetime import datetime, timedelta
def meal():
    time_str = input("What time is it? ")
    time = datetime.strptime(time_str, "%H:%M")

    # Start and end times
    breakfast_start = datetime.strptime("07:00", "%H:%M")
    breakfast_end = datetime.strptime("08:00", "%H:%M")

    # Generate list of times at one-minute intervals
    # breakfast_range = []
    # current_time = breakfast_start
    # while current_time <= breakfast_end:
    #     breakfast_range.append(current_time.strftime("%H:%M"))
    #     current_time += timedelta(minutes=1)
    
    lunch_start = datetime.strptime("12:00", "%H:%M")
    lunch_end = datetime.strptime("13:00", "%H:%M")

    # lunch_range = []
    # current_time = lunch_start
    # while current_time <= lunch_end:
    #     lunch_range.append(current_time.strftime("%H:%M"))
    #     current_time += timedelta(minutes=1)

    dinner_start = datetime.strptime("18:00", "%H:%M")
    dinner_end = datetime.strptime("19:00", "%H:%M")

    # dinner_range = []
    # current_time = dinner_start
    # while current_time <= dinner_end:
    #     dinner_range.append(current_time.strftime("%H:%M"))
    #     current_time += timedelta(minutes=1)

    if breakfast_start <= time <= breakfast_end:
        print("Breakfast time!")
    elif lunch_start <= time <= breakfast_end:
        print("Lunch time!")
    elif dinner_start <= time <= breakfast_end:
        print("Dinner time!")
    else:
        print(None)

meal()"""


# ---PROBLEM_SET_2---
#1 CamelCase
"""import re

case = input("camelCase: ")

result = re.sub(r'([a-z])([A-Z])', r'\1_\2', case)
print(f"snake_case: {result}")"""

#2 Coke Machine
"""total = 0
target = 50
print("Insert coins (accepted: 1, 5, 10, 25):")
while total < target:
    try:
        coins = int(input("Insert coin: "))
        if coins in [1, 5, 10, 25]:
            total += coins
            print(f"Total inserted: {total}")
        else:
            print("Invalid coin. Please insert(1, 5, 10 or 25)")
    except ValueError:
        print("please insert valid coins!")

if total > target:
    print(f"Amount reached! Returning change: {total - target}")
else:
    print("Amount reached exactly! No change to return.")"""

#3 Just Setting Up My Twttr
"""a = input("Input: ")
vowels = "aeiouAEIOU"
result = "".join([ch for ch in a if ch not in vowels])
print(f"Output: {result}")"""

#4 Vanity Plates
"""def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if not(2 <= len(plate) <= 6):
        return False
    
    if not plate[:2].isalpha():
        return False
    
    if not plate.isalnum():
        return False
    
    for i, ch in enumerate(plate):
        if ch.isdigit():
            if ch == '0':
                return False
            if not plate[i:].isdigit():
                return False
            break
    return True
if __name__ == "__main__":      
    main()"""

#5 Nutritions Facts
"""fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 60,
    "honeydew" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plum" : 70,
    "strawberries" : 50,
    "sweet" : 100,
    "tangerine" : 50,
    "watermelon" : 80
}
choose = input("Items: ")
if choose in fruits:
    print(f"Calories: {fruits[choose]}")
else:
    print("Items not in the fruits!")"""


# PRACTICE_SET (FILE I/O)
#1 word count
"""with open("C:\\Users\\Lenovo\\classroom\\word.txt") as f:
    data = f.read()
    print(data)
    print(f"Length of the file: {len(data)}")
    print(f"No of words: {len(data.split())}")
    print(f"No of lines: {len(data.splitlines())}")"""

#2 save notes
"""import csv

file_path = "C:\\Users\\Lenovo\\classroom\\students.csv"
with open(file_path, mode="a", newline='') as f:
    writer = csv.writer(f)
    while True:
        ask = input("Write something or type 'quit' to exit: ").strip().lower()
        if ask == "quit":
            break
        writer.writerow([ask])"""

#3 CSV scoreboard
"""import csv

name = input("Input name: ")
score = int(input("Input score: "))
file_path = "C:\\Users\\Lenovo\\classroom\\students.csv"
with open(file_path, mode="a+", newline='') as f:
    writer = csv.writer(f)
    writer.writerow([name, score])

    f.seek(0)
    data = csv.reader(f)
    for row in data:
        print(row)"""
    
# ---PROBLEM_SET_3---
#1 Fuel Gauge
"""def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y or y == 0:
                continue
            percentage = round((x / y) * 100)
            break
        except (ValueError, ZeroDivisionError):
            continue

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

main()"""


#2 Felipe's Taqueria
"""items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadila": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    choice = input("choose item or type 'q' to quit: ")

    if choice.lower() == "q":
        print("Have a GoodDay!")
        break

    choice = choice.title()

    if choice in items:
        total += items[choice]
        print(f"Total: ${total:.2f}")
    else:
        print("Please pick something from the menu!")"""


#3 Grocery List
"""groceries = {}

while True:
    try:
        items = input().strip().lower()
    
        if items in groceries:
            groceries[items] += 1
        else:
            groceries[items] = 1
    except EOFError:
        break

    for items in sorted(groceries):
        print(f"{groceries[items]} {items.upper()}")"""


#4 Outdated
"""months = [
    "January", "February", "March", "April", "May", "June", "July",
      "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{int(year)}-{month:02}-{day:02}")
            break
    except:
        try:
            month_day, year = date.split(",")
            month_name, day = month_day.strip().split(" ")
            day = int(day)
            if month_name in months and 1 <= day <= 31:
                month = months.index(month_name) + 1
                print(f"{int(year.strip())}-{month:02}-{day:02}")
                break
        except:
            continue"""

# ---PROBLEM_SET_4---
#1  


# PYTHON MINI TEST
#1 Write a program that takes a number and prints whether it's even or odd.
"""n = int(input("Enter num: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")"""

#2 write a program that takes a string and prints it in reverse order (without using built-in reverse() function).
"""s = input("Enter word: ")

print(s[::-1])"""

#3 write a program to find the largest number in a list: nums = [4, 9, 1, 7, 12, 3].
"""nums = [4, 9, 1, 7, 12, 3]

n = 0
for i in nums:
    if i > n:
        n = i
    
print(n)"""

#4 write a function in_palindrome(word) that returns True if the word is a palindrome, otherwise False.
"""def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
print(palindrome(word="wow"))"""
     
#5 Write a function factorial(n) that uses recursion.
"""def factorial():
    n = int(input("Enter num: "))
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
factorial()"""

#6 Given a list of numbers, return a new list with only even numbers.
"""list = [1, 3, 5, 9, 12, 18, 16]

for i in list:
    if i % 2 == 0:
        print(i)"""

#7 Write a program that opens a file data.txt, reads its contents, and prints each line in uppercase.
"""file_path = "C:\\Users\\Lenovo\\classroom\\data.txt"

with open(file_path, mode="r")as f:
    for line in f:
        print(line.strip().upper())"""

#8 write a function that counts how many times each word appears in a sentence.

#9 write a function fibonacci(n) that returns the nth fibonacci number.

#10 Bonus: Write a program to print triangle pattern like this for n=4.
"""n = 4
for i in range(n+1):
    print('*' * i)
    i += 1"""