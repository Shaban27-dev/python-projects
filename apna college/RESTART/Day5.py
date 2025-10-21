#   LOOPS IN PYTHON
#  WHILE LOOPS
"""i = 1
while i <= 5:
    print(i)
    i += 1
print("loop ended")"""

#  Q1)  PRINT NUMBERS FROM 1 TO 100.
"""i = 1
while i <= 100:
    print(i)
    i += 1
print("loops ended")"""

#  Q2)  PRINT NUMBERS FROM 100 TO 1.
"""i = 100
while i >= 1:
    print(i)
    i -= 1
print("loop ended")"""

#  Q3)  PRINT THE MULTIPLICATION TABLE OF A NUMBER N.
"""i = int(input("enter a num :"))
n = 1
while n <= 10:
    print(i * n)
    n += 1
print("loop ended")"""

#  Q4)  PRINT THE ELEMENTS OF THE FOLLOWING LIST USING A LOOP.
#       (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
"""nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1"""

#  Q5)  SEARCH FOR A NUMBER X IN THIS TUPLE USING WHILE LOOP.
"""nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 25
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i) 
    i += 1"""

# BREAK & CONTINUE
"""i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("end of loop")"""

"""i = 1
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1"""

"""i = 1
while i <= 100:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1"""

#  FOR LOOP
"""list  = [1, 2, 3, 4, 5]

for el in list:
    print(el)""" 

"""str = "apnacollege"

for el in str:
    if(el == 'o'):
        print("o found")
        break
    print(el)
else: # works only when entire loop ends
    print("end")"""

#  Q6)  PRINT THE ELEMENTS OF THE FOLLOWING LIST USING FOR LOOP.
#       [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)"""

#  Q7)  SEARCH FOR A NUMBER X IN THIS TUPLE USING FOR LOOP.
#       [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""tup = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 64
idx = 0
for el in tup:
    if(el == x):
        print("found at idx", idx)
    idx += 1"""

#  RANGE()
"""for el in range(5):  #stop
    print(el)

for el in range(1,5):  #start?, stop
    print(el)

for el in range(1,10,2):  #start?, stop, step?
    print(el)"""

#  Q8)  PRINT NUMBERS FROM 1 TO 100.
"""for i in range(1,100):
    print(i)"""

#  Q9)  PRINT NUMBERS FROM 100 TO 1.
"""for i in range(100, 0, -1):
    print(i)"""

# #  Q10)  PRINT THE MULTIPLICATION TABLE OF A NUMBER N.
"""for i in range(3, 31, 3):
    print(i)"""

"""n = int(input("enter num :"))

for i in range(1, 11):
    print(n * i)"""

#  pass statement
"""for i in range(5):
    pass

if i > 5:
    pass

print("some useful work")"""

#  Q11)  WAP TO FIND THE SUM OF FIRST N NUMBERS.(USING WHILE)
"""n = int(input("enter a num:"))

sum = 0
for i in range(1, n+1):
    sum += i
print(sum)"""

"""n = int(input("enter a num :"))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)

n = int(input("enter a num :"))"""

#  Q12)  WAP TO FIND THE FACTORIAL OF FIRST N NUMBERS.(USING range)
"""n = int(input("enter a num :"))

fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)"""

"""n = 5

fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)"""