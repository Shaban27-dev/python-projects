# LOOPS
"""i = 0
while i <= 4:
    print("Shaban")
    i += 1"""

# print("meow\n" * 3, end="")

"""while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")"""

"""def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break

    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()"""


# LISTS
"""students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])"""

"""students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for i in students:
    print(i, students[i], sep=": ")"""

"""students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=": ")"""


# MARIO
"""def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")
    
main()"""

"""def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()"""

"""def main():
    print_square(3)

def print_square(size):

    # For each row in square
    for i in range(size):

            # Print brick
            print("#" * size)

main()"""


#  EXCEPTIONS
"""def get_int():
    while True:
        try: 
            x = float(input("What's x? "))
        except ValueError:
            pass
        else:
            return x
            break

get_int()"""
