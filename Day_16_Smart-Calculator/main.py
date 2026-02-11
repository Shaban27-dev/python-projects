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