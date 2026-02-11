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