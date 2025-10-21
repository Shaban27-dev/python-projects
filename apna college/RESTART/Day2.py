"""str1 = "this is a string.\nwe are creating it in python."
print(len(str1))"""

"""str = "apna college"
print(str[5:])"""

"""str = "apple"
print(str[-5:-2])"""

#   STRING FUNCTIONS

"""str = "i am a coder."
print(str.endswith("er."))
print(str.capitalize())
str = str.replace("am", "are")
print(str)
print(str.find("a"))
print(str.count("a"))"""

# Q1)   WAP TO INPUT USER'S FIRST NAME & PRINT ITS LENGTH.
"""name = input("enter name :")
print(len(name))""" 
 
# Q2)   WAP TO FIND THE OCCURENCE OF '$' IN A STRING.
"""str = "hey this is shaban $ and i am learning python $."
print(str.count("$"))"""

#   CONDITIONAL STATEMENTS
"""light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")

print("end of code")"""

"""marks = int(input("enter marks :"))

if (marks >= 90):
    print("grade A")
elif(marks < 90 and marks >= 80):
    print("grade B")
elif(marks < 80 and marks >= 70):
    print("grade C")
else:
    print("grade D")"""

#nesting
"""age = 60

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")"""

# Q3)   WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN.
"""num = int(input("enter num :"))

if(num%2 == 0):
    print("Even")
else:
    print("Odd")"""

# Q4)   WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER.
"""a = int(input("enter num1 :"))
b = int(input("enter num2 :"))
c = int(input("enter num3 :"))

if(a > b and a > c):
    print("a is greatest")
elif(b > c):
    print("b is greatest")
else:
    print("c is greatest")"""

# Q5)   WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT.
"""a = int(input("enter num :"))

if(a % 7 == 0):
    print("multiple of 7")
else:
    print("not multiple")"""