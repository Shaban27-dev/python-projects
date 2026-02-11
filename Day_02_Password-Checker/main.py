#          DAY_2
# Password Strength Checker (if length < 8 → weak, else strong).
password = input("Enter password: ")

if len(password) >= 8:
    print("Strong password!")
else:
    print("Weak password!")