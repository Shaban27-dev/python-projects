# VARIABLES

"""# Ask user for their name and removes whitespace from str and capitalizes it.
name = input("what's you name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")""" 


# INT
"""x = int(input("What's x? "))
y = int(input("What's y? "))

sum = x + y

print(sum)"""

"""x = float(input("enter a num: "))
y = float(input("enter a num: "))

z = round(x / y, 2)

print(f"{z:.2f}")"""


# FUNCTIONS
"""def hello(to="world"):
    print("hello,", to)

hello()
name = input("What's your name? ")
hello(name)"""


"""def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()"""


"""def calculator():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n ** 2

calculator()"""