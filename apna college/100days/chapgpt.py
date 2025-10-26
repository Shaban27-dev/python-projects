#          DAY-1
#1 Write a program to add two numbers.
"""a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))
c = a + b
print(c)"""

#2 Convert celsius to fahrenheit.
"""a = float(input("Enter temperature: "))
b = (a * 1.8) + 32
print(f"Temperature in farenheite is: {b}")"""

#3 Odd/even checker.
"""a = int(input("Enter num: "))
if a % 2 == 0:
    print("Even")
else:
    print("Odd")"""


#          DAY-2
#1 Write a program to find the largest of 3 numbers.
"""a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
c = int(input("Enter third num: "))

if a > b and a > c:
    print(f"Largest among {a, b, c} is {a}")
elif b > c:
    print(f"Largest amont {a, b, c} is {b}")
else:
    print(f"Largest among {a, b, c} is {c}")"""

#2 Write a program for grade calculator (marks = A/B/C/D).
"""try:
    grade = int(input("Enter the score: "))
except ValueError:
    print("The grade must be a positive integer!")

if 90 <= grade <= 100:
    print("You got A")
elif 80 <= grade < 90:
    print("You got B")
elif 70 <= grade < 80:
    print("You got C")
else:
    print("You got D")"""


#          DAY-3
#1 Write a code to print multiplication table of a number.
"""n = int(input("Enter num: "))

for i in range(0, 11):
    print(n * i)
    i += 1"""

#2 Write a code to print the sum of digits of a number.
"""n = int(input("Enter num: "))
total = 0

while n > 0:
    digit = n % 10   # This is to get the last digit of {n}.   E.G: 1234 % 10 = 4.
    total += digit   # Then the last digit gets add to total
    n = n // 10   # This is to get all digits except the last one and it also gets add to total.   E.G: 1234 // 10 = 123.

print(f"Sum of digits: {total}")"""

#3 write a code for factorial using loop.
"""n = int(input("Enter num: "))
fact = 1

for i in range(1, n+1):
    fact *= i
print(fact)

n = int(input("Enter num: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)"""


#          DAY-4
#1 Write a function to check whether the number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        return True
    
print(is_prime(107))
print(is_prime(25))
print(is_prime(35))
    
#2 Write a function to reverse a string (without slicing.)
"""def reverse_string(s):
    return ''.join(reversed(s))

print(reverse_string("hello"))"""

"""def reverse_string(s):
    reversed_string = ""
    index = len(s) - 1
    while index >= 0:
        reversed_string += s[index]
        index -= 1
    return reversed_string

print(reverse_string("shaban"))""" 
