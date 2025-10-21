#    FUNCTIONS & RECURSION

# function definition
"""def calc_sum(a , b):  #parameters
    sum = a + b
    print(sum)
    return sum

calc_sum(9, 80)"""  #function call; arguments

"""def printHello():
    print("hello")

printHello()
printHello()"""

#average of 3 numbers
"""def calc_average(a , b, c):
    average = (a + b + c)/3
    print(average)
    return average

calc_average(2, 4, 9)"""

#default parameters
"""def calc_prod(a, b=7):
    prod = a * b
    print(prod)
    return prod

calc_prod(8)"""

#  Q1)  WAP TO PRINT THE LENGTH OF A LIST. (LIST IS THE PARAMETER)
"""names = ["shaban", "sarib", "zaid", "rehan", "asad"]

def print_len(list):
    print(len(list))

print_len(names)
"""
"""nums = [2, 3, 4, 5, 5]

def print_len(list):
    print(len(list))

print_len(nums)"""

#  Q2)  WAP TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE.(LIST IS THE PARAMETER)
"""heroes = ["batman", "superman", "spiderman", "ironman", "thor"]

def print_list(list):
    for el in heroes:
        print(el, end= " ")

print_list(heroes)
print()"""

#  Q3)  WAP TO FIND THE FACTORIAL OF N.(N IS THE PARAMETER)
"""def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(5)"""

#  Q4)  WAP TO CONVERT UST TO INR.
"""def converter(INR_val):
    usd_val = INR_val/ 83
    print(INR_val, "inr =", usd_val, "usd")

converter(830)"""

"""def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val, "usd =", inr_val, "inr")

converter(15)"""

#  Q5)  WAP TO INPUT A NUMBER. PRINT ODD IF NUM IS ODD, ELSE EVEN.
"""n = int(input("enter a num :"))

def print_oddeven(n):
    if (n % 2 == 0):
        print("EVEN")
    else:
        print("ODD")
print_oddeven(n)"""

# Recursion
"""def show(n):
    if(n == 6):
        return
    print(n)
    show(n+1)

show(1)"""

"""def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n -1) * n

print(fact(6)) """

#  Q6)  WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS.
"""def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n
print(sum(5)) """

#  Q7)  WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENTS IN A LIST.
#       HINT: USE LIST & INDEX AS PARAMETERS. 
"""var = ["names", "age", "roll no", "class"]

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)

print_list(var, )

names = ["shaban", "sarib", "taush", "sharukn"]

def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)

print_list(names)""" 