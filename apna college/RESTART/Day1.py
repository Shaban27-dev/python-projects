# print("hello world","my age is 20")

"""name = "shaban"
age = 20
price = 25.99

print("my name is :", name)
print("my age is :", age)"""

# PRINT SUM
"""a = 2
b = 5
sum = a + b
print(sum)"""

# EXPRESSION EXECUTION
"""a,b = 3, 4
txt = "@"
print(2 * txt * 3)"""

"""a,b = "2",3
txt = "@"
print((a + txt)* b)"""

"""a,b = 2,3
c = 4
print(a+b*c)"""

"""a,b = 10,5.0
c = a*b
print(c)"""

"""a,b = 1,2
c = a/b
print(c)"""

"""a,b = 1.5,3
c = a//b
print(c, a/b)"""

"""a,b = 12,5
c = a//b
print(c)"""

"""a,b = -12, 5
c = a//b
print(c)"""

"""a,b = 12,-5
c = a//b
print(c)"""

"""a,b = -5,2
c = a%b
print(c)"""

"""a,b = 5,2
c = a%b
print(c)"""

"""a,b = 5,-2
c = a%b
print(c)"""

#   INPUT IN PYTHON
"""# string input
name = input("name : ")
# int input
age = int(input("age : "))
# float input
price = float(input("price : "))
print(name, age, price)"""

#   CONDITIONAL STATEMENTS
"""if-elif-else(SYNTAX)

if(condition):
    statement1
elif(condition):
    statement2
else:
    statementN"""

"""light = input("light :")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("wait")
elif(light == "green"):
    print("go")
else:
    print("light is broken")"""

"""marks = int(input("enter marks :"))
if(marks >= 90):
    print("A")
elif(marks <= 90 and marks >=80):
    print("B")
elif(marks <= 80 and marks >= 70):
    print("C")
else:
    print("D")"""

#   PRACTICE TIME
# A = 5 & G = M
# A = 2 & G = F
"""a = int(input("A :"))
g = input("M/F :")
if((a == 1 or a == 2)and g == "m"):
    print("fee is 100")
elif(a == 3 and a == 4 or g == "f"):
    print("fee is 200")
elif(a == 5 and g == "m"):
    print("fee is 300")
else:
    print("no fee")"""

# TERNARY OPERATOR
"""food = input("food :")
eat = "yes" if food == "cake" else "no"
print(eat)"""

"""food = input("food :")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")"""

"""age = int(input("age :"))
vote = ("yes", "no") [age <= 18]
print(vote)"""

"""sal = float(input("salary :"))
tax = sal*(0.1, 0.2) [sal>=50000]
print(tax)"""

#   BEST PRACTICES
# SIMPLE INSTRUCTIONS
# ONE INSTRUCTION PER TASK
# SHORT & MEANINGFUL VARIABLE NAMES
# USE APPROPRIATE COMMENTS
# AVOID COMPLEX EXPRESSRION
 
#   TYPES OF OPERATORS

#arithmetic operators
"""a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)"""

#relational operators
"""a = 50 
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)"""

#assignment operators
"""num = 10
num = num + 10
num += 10
num -= 10
num *= 10
num /= 10
num %= 10
num **= 10
print("num :", num)"""

#logical operators
"""a = 50
b = 30
print(not False)
print(not (a > b))

val1 = True
val2 = False
print("AND operator :", val1 or val2)

print("OR operator :", (a == b) or (a > b))"""

#type conversion
"""a = 2
b = 4.25

sum = a + b
print(sum)"""

"""a,b = 1,"2"
c=int(b)
print(a + c)"""

"""name = input("enter name :")
age = int(input("enter age :"))
marks = float(input("enter marks :"))
print("my name is", name, ",i am", age, "years old", "and i got", marks, "marks in maths")"""

# Q1)  WAP TO INPUT 2 NUMBERS & PRINT THEIR SUM.
"""a = int(input("enter num1 :"))
b = int(input("enter num2 :"))
sum = a + b
print(sum)"""

# Q2)  WAP TO INPUT SIDE OF A SQUARE & PRINT ITS AREA.
"""side = float(input("enter side :"))
area = side * side
print(area)"""

# Q3)  WAP TO INPUT 2 FLOATING POINT NUMBERS & PRINT THEIR AVERAGE.
"""a = float(input("enter num1 :"))
b = float(input("enter num2 :"))
average = (a+b)/2
print(average)"""

# Q4)  WAP TO INPUT 2 INT NUMBERS, A AND B.
#      PRINT TRUE IF A IS GREATER THAN OR EQUAL TO B. IF NOT PRINT FALSE.
"""a = int(input("enter num1 :"))
b = int(input("enter num2 :"))

if(a > b):
    print(True)
else:
    print(False)"""