#               LECTURE 1

#  WRITE A PROGRAM TO INPUT 2 NUMBERS & PRINT THEIR SUM.
"""a = int(input("enter a num :"))
b = int(input("enter a num :"))

sum = a + b
print(sum)"""

#  WAP TO INPUT SIDE OF A SQUARE AND PRINT ITS AREA.
"""side = float(input("enter side :"))
area = side * side
print(area)"""

#  WAP TO INPUT 2 FLOATING POINT NUMBERS AND PRINT THEIR AVERAGE.
"""a = float(input("enter num :"))
b = float(input("enter num :"))
average = (a + b)/2
print(average)"""

#  WAP TO INPUT 3 INT NUMBERS, A AND B.
#  PRINT TRUE IF A IS GREATER THEN OR EQUAL TO B. IF NOT PRINT FALSE.
"""a = int(input("enter num :"))
b = int(input("enter num :"))
c = int(input("enter num :"))

if(a > b and a > c):
    print("a is greatest")
elif(b > c):
    print("b is greatest")
else:
    print("c is greatest")"""


#               LECTURE 2

#  WAP TO INPUT USER'S FIRST NAME AND PRINT ITS LENGTH.
"""a = int(input("enter name :"))
print(len(a))"""

#  WAP TO FIND THE OCCURRENCE OF '$' IN A STRING.
"""a = "hello, i am shaban $ and i am learning $ python"
print(a.count("$"))"""

#  WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS Odd OR EVEN.
"""a = int(input("enter num :"))
if(a%2 == 0):
    print("EVEN")
else:
    print("ODD")"""

#  WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER.
"""a = int(input("enter num :"))
b = int(input("enter num :"))
c = int(input("enter num :"))

if(a > b and a > c):
    print("a is greatest")
elif(b > c):
    print("b is greatest")
else:
    print("c is greatest")"""

#  WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT.
"""a = int(input("enter num :"))

if(a % 7 == 0):
    print("multiple of 7")
else:
    print("not multiple")"""


#               LECTURE 3

#  WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FOVORITE MOVIES AND STORE THEM IN A LIST.
"""movie1 = input("enter a movie :")
movie2 = input("enter a movie :")
movie3 = input("enter a movie: ")

list = [movie1, movie2, movie3]
print(list)"""

#  WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS.(HINT: USE COPY() METHOD)
#  [1,2,3,2,1]  [1, "ABC", "ABC", 1]
"""list = [1, 2, 3, 4, 3, 2, 1]

copied_list =list.copy()
copied_list.reverse()
if(list == copied_list):
    print("palindrome")
else:
    print("not palindrome")"""


#  WAP TO COUNT THE NUMBER OF STUDENTS WITH THE "A" GRADE IN THE FOLLOWING TUPLE.
#  ["C", "D", "A", "A",  "B", "B", "A"]
"""tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))"""

#  STORE THE ABOVE VALUES IN A LIST & SORT THEM FROM "A" TO "D".
"""list = ["C", "D", "A", "A",  "B", "B", "A"]
list.sort()
print(list)"""


#               LECTURE 4

#  STORE FOLLOWING WORD MEANINGS IN A PYTHON DICTIONARY:
#  TABLE: "A PIECE OF FURNITURE", "LIST OF FACTS AND FIGURES"
#  CAT: "A SMALL ANIMAL"
"""dict = {
    "table" : ("a piece of furniture", "list of facts and figures"),
    "cat" : "a small animal"
}
print(dict)"""

#  YOU ARE GIVEN A LIST OF SUBJECTS FOR STUDENTS. ASSUME ONE CLASSROOM IS REQUIRED FOR 1 SUBJECT.
#  HOW MANY CLASSROOMS ARE NEEDED BY ALL STUDENTS.
#  "PYTHON", "JAVA", "C++", "PYTHON", "JAVASCRIPT", "JAVA", "PYTHON", "JAVA", "C++", "C"
"""subjects = {"PYTHON", "JAVA", "C++", "PYTHON", "JAVASCRIPT", "JAVA", "PYTHON", "JAVA", "C++", "C"}
print(len(subjects))
print(type(subjects))"""

#  WAP TO ENTER MARKS OF 3 SUBJECTS FROM THE USER AND STORE THEM IN A DICTIONARY. START WITH AN EMPTY DICTIONARY & ADD ONE BY ONE.
#  USE SUBJECT NAME AS KEY AND MARKS AS VALUE.
"""null_dict = {}
null_dict["phy"] = 88
null_dict["chem"] = 86
null_dict["math"] = 87
print(null_dict)"""

#  FUGURE OUT A WAY TO STORE 9 & 9.0 AS SEPARATE VALUES IN THE SET.
#  (YOU CAN TAKE HELP OF BUILT-IN DATE TYPES)
"""set = { 9, "9.0"}
print(set)"""


#               LECTURE 5

#  PRINT NUMBERS FROM 1 TO 100.
"""i = 1
while i < 101:
    print(i)
    i += 1"""

#  PRINT NUMBERS FROM 100 TO 1.
"""i = 100
while i > 0:
    print(i)
    i -= 1"""

#  PRINT THE MULTIPLICATION TABLE OF A NUMBER N.
"""n = int(input("enter a num :"))
i = 1
while i < 11:
    print(n * i)
    i += 1"""

#  PRINT THE ELEMENTS OF THE FOLLOWING LIST USING A LOOP:
#  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while(idx < len(list)):
    print(list[idx])
    idx += 1"""

#  SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP:
#  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 81
idx = 0

while idx < len(list):
    if(list[idx] == x):
        print("found at :", idx) 
    idx += 1"""
    

#  PRINT THE ELEMENTS OF THE FOLLOWING LIST USING A LOOP:  USING FOR
#  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
"""list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in list:
    print(el)"""

#  SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP:  USING FOR
#  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 64
idx = 0

for el in list:
    if(el == x):
        print("found at idx :", idx)
    idx += 1"""
    


#  PRINT NUMBERS FROM 1 TO 100.  USING FOR & RANGE()
"""for i in range(101):
    print(i)"""

#  PRINT NUMBERS FROM 100 TO 1.  USING FOR & RANGE()
"""for i in range(100, 0, -1):
    print(i)"""

#  PRINT THE MULTIPLICATION TABLE OF A NUMBER N.  USING FOR & RANGE()
"""for i in range(0, 51, 5):
    print(i)"""

#  WAP TO FIND THE SUM OF FIRST N NUMBERS.(USING WHILE)
"""n = int(input("enter num :"))
sum = 0


for i in range(1, n + 1):
    sum += i
print(sum)"""

"""n = int(input("enter a num :"))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print(sum)"""

#  WAP TO FIND THE FACTORIAL OF FIRST N NUMBERS.(USING FOR)
"""n = int(input("enter a num :"))
fact = 1

for i in range(1, n+1):
    fact*=i
print(fact)"""

"""n = int(input("enter a num :"))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1
print(fact)"""


#               LECTURE 6

#  WAP TO PRINT THE AVERAGE OF 3 NUMBERS.
"""def calc_average(a, b, c):
    average = (a + b + c) / 3
    print(average)
    return average

calc_average(9,8,7)"""

#  WAP TO PRINT THE LENGTH OF A LIST. (LIST IS THE PARAMETER)
"""names = ["shaban", "sarib", "saif", "sam"]
def print_len(list):
    print(len(list))

print_len(names)"""

#  WAP TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE.(LIST IS THE PARAMETER)
"""movies = ["batman", "superman", "ironman", "spiderman", "thor"]
def print_list(list):
    for el in list:
        print(el, end = " ")

print_list(movies)"""

#  WAP TO FIND THE FACTORIAL OF N. (N IS THE PARAMETER)
"""n = int(input("enter num :"))

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(n)"""

#  WAP TO CONVERT USD TO INR.
"""def convertor(inr_val):
    usd_val = inr_val / 83
    print(inr_val, "INR =", usd_val, "USD")

convertor(830)

def convert(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

convert(15)"""

#  WAP TO INPUT A NUMBER AND PRINT "ODD" IF NUM IS ODD, ELSE PRINT "EVEN"
"""n = int(input("enter num :"))

def print_oddeven(n):
    if(n % 2 == 0):
        print("EVEN")
    else:
        print("ODD")
    
print_oddeven(n)"""

#  WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS.
"""def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n
print(sum(5))

def diff(n):
    if (n == 0):
        return 0
    return diff(n-1) - n
print(diff(5))"""

#  WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENTS IN A LIST.
#       HINT: USE LIST & INDEX AS PARAMETERS.
"""cars = ["porsche", "bmw", "audi", "mercedes", "mclaren"]

def print_list(list, idx = 0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list, idx + 1)
print_list(cars)"""

"""names = ["shaban", "sarib", "arsil", "taush"]

def print_list(list, idx = 0):
    if(idx ==len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)
print_list(names)"""


#               LECTURE 7

# Q1)  CREATE A NEW FILE "PRACTICE.TXT" USING PYTHON. ADD THE FOLLOWING DATA IN IT:
# HI EVERYONE
# WE ARE LEARNING FILE I/O
# USING JAVA
# I LIKE PROGRAMMING IN JAVA
"""f = open("apna college\\RESTART\\demo.txt", "a")
f.write("i like programming in java")
f.write("\ncurrently learning python")

f = open("apna college\\RESTART\\demo.txt", "w")
f.write("HI EVERYONE\nWE ARE LEARNING FILE I/O")
f.write("\nUSING JAVA\nI LIKE PROGRAMMING IN JAVA")"""

# Q2)  WAF THAT REPLACE ALL OCCURRENCES OF "JAVA" WITH "PYTHON" IN ABOVE FILE.
"""with open("apna college/RESTART/demo.txt", "r") as f:
    data = f.read()

new_data = data.replace("JAVA", "PYTHON")
print(new_data)

with open("apna college/RESTART/demo.txt", "w") as f:
    f.write(new_data)"""

# Q3)  SEARCH IF THE WORD "LEARNING" EXISTS IN THE FILE OR NOT.
"""word = "LEARNING"
with open("apna college/RESTART/demo.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("FOUND")
    else:
        print("NOT FOUND")"""

"""def check_for_word():
    word = "PYTHON"
    with open("apna college/RESTART/demo.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")

check_for_word()"""

# Q4)  WAF TO FIND IN WHICH LINE OF THE FILE DOES THE WORD "LEARNING" OCCUR FIRST.
#      PRINT -1 IF WORD NOT FOUND.
"""def check_for_word():
    word = "LEARNING"
    data = True
    line_no = 1
    with open("apna college/RESTART/demo.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
print(check_for_word())"""

"""def search_for_word():
    word = "PYTHON"
    data = True
    line_no = 1
    with open("apna college/RESTART/demo.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
        return -1
print(search_for_word())"""

# Q5)  FROM A FILE CONTAINING NUMBERS SEPARATED BY COMMA, PRINT THE COUNT OF EVEN NUMBERS.
"""count = 0
with open("apna college/RESTART/demo.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)"""


#               LECTURE 8

# Q1)  CREATE STUDENT CLASS THAT TAKES NAME & MARKS OF 3 SUBJECTS AS ARGUMENTS IN CONSTRUCTOR.
#      THEN CREATE A METHOD TO PRINT THE AVERAGE.
"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("hey", self.name, "your avg is :", sum/3)

s1 = Student("shaban", [89, 87, 85])
s1.get_avg()

s2 = Student("sarib", [98, 97, 96])
s2.get_avg()"""

"""class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_total(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("hello", self.name, "your total is :", sum)

s1 = Student("shaban", [91, 90 ,89])
s1.get_total() """

# Q2)  CREATE ACCOUNT CLASS WITH 2 ATTRIBUTES - BALANCE & ACCOUNT N0.
#      CREATE METHODS FOR DEBIT, CREDIT & PRINTING THE BALANCE.
"""class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("RS :", amount, "was debited.")
        print("Total balance :", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("RS :", amount, "is credited.")
        print("Total balance :", self.get_balance())
    
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, "12354")
acc1.debit(2000)
acc1.credit(5000)""" 


#               LECTURE 9

# Q1)  DEFINE A CIRCLE CLASS TO CREATE A CIRCLE WITH RADIUS R USING THE CONSTRUCTOR.
#      DEFINE AN AREA() METHOD OF THE CLASS WHICH CALCULATES THE AREA OF THE CIRCLE.
#      DEFINE A PERIMETER() METHOD OF THE CLASS WHCIH ALLOWS YOU TO CALCULATE THE PERIMETR OF THE CIRCLE.
"""class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (22/7) * self.radius
    
    def perimeter(self):
        return 2 * (22/7) * self.radius ** 2
    
c1 = Circle(8)
print(c1.area())
print(c1.perimeter())""" 

# Q2)  DEFINE A EMPLOYEE CLASS WITH ATTRIBUTES ROLE, DEPARTMENT & SALARY. THIS CLASS ALSO HAS A SHOWDETAILS() METHOD.
#      CREATE AN ENGINEER CLASS THAT INHERITS PROPERTIES FROM EMPLOYEES & has additional attributes : name & age.
"""class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role :", self.role)
        print("dept :", self.dept)
        print("salary :", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super(). __init__("Engineer", "IT", "90000")

e1 = Engineer("shaban", 20)
print(e1.name)
print(e1.age)
print(e1.showDetails())"""

# Q3)  CREATE A CLASS CALLED ORDER WHICH STORES ITEM & ITS PRICE.
#      USE DUNDER FUNCTION__GT__() TO CONVEY THAT:
#          ORDER1 > ORDER2 IF PRICE OF ORDER1 > PRICE OF ORDER2   
"""class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("chips", "20")
odr2 = Order("chocolate", "10")
print(odr1 > odr2)"""


#               MINI PROJECT
#  GUESS THE NUMBER
"""import random

target = random.randint(0, 100)

while True:
    userChoice = input("Guess the num or quit(Q) : ")
    if(userChoice == "QUIT"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("your guess is correct.")
        break
    elif(userChoice < target):
        print("Guess is < target")
    else:
        print("Guess is > target")
    
print("----GAME OVER----")"""

#  RANDOM PASSWORD GENERATOR
"""import random
import string

pass_len = 10
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [function for i in range(n)]

# password = "".join([random.choice(charValues) for i in range(pass_len)])

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("your password is :", password)"""  