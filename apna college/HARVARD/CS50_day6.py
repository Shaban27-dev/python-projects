#   ---FILE I/O---
"""names = []

for _ in range(3):
    names.append(input("What's you name? "))

for name in sorted(names):
    print(f"hello, {name}")"""


"""with open("C:\\Users\\Lenovo\\classroom\\file.txt", "r") as file:
    # file.write(f"{name}\n")
    for line in file:
        print("hello,", line.rstrip())"""

"""names = []

with open("C:\\Users\\Lenovo\\classroom\\file.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True): #Descending order
    print(f"hello, {name}")

print(len(name))"""

"""with open("C:\\Users\\Lenovo\\classroom\\students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")"""

"""students = []

with open("C:\\Users\\Lenovo\\classroom\\students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}
        students.append(student)

# def get_name(student):
#     return student["name"]

for student in sorted(students, key=lambda student: student["name"]): 
    print(f"{student['name']} is from {student['home']}")"""

"""import csv

students = []

with open("C:\\Users\\Lenovo\\classroom\\students.csv") as file:
    reader = csv.DictReader(file) # Even if i reverse the values in csv file it'll still show the same input. we just need to change the header and read the csv file as DictReader
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}") """

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("C:\\Users\\Lenovo\\classroom\\students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
    
