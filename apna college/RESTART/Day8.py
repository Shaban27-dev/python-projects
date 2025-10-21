#   OOPS (PART 1)
"""class Student:
        name = "shaban"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)"""

"""class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)"""


#  __init__ Function
#  Constructor
"""class Student:
    
    def __init__(self, name, marks ):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")
   
s1 = Student("shaban", 93)
print(s1.name, s1.marks)

s2 = Student("sarib", 87)
print(s2.name, s2.marks)"""

#  Class & Instance Attributes
"""class Student:
    college_name = "ABC College"
    name = "anythin"  #class attr
    
    def __init__(self, name, marks ):
        self.name = name  #obj attr > class attr
        self.marks = marks
        print("adding new student in Database..")
   
s1 = Student("shaban", 93)
print(s1.name, s1.marks)"""

#  Methods
"""class Student:
    college_name = "ABC College"
    name = "anythin"  #class attr
    
    def __init__(self, name, marks ):
        self.name = name  #obj attr > class attr
        self.marks = marks
       
    def welcome(self):
        print("welcome student,", self.name)

    def hello(self):
        print("hello student,", self.name)

    def get_marks(self):
        return self.marks
   
s1 = Student("shaban", 93)
s1.welcome()
print(s1.get_marks())

s2 = Student("sarib", 87)
s2.hello()
print(s2.get_marks())"""

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
        print("hey", self.name, "your avg is", sum/3)

s1 = Student("shaban", [89, 87, 85])
s1.get_avg()

s2 = Student("sarib", [98, 97, 96])
s2.get_avg()"""

"""class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def get_total(self):
        sum =0
        for val in self.marks:
            sum += val
        print("hello", self.name, "your age is", self.age, "your total score is", sum)

s1 = Student("saif", 20, [98, 89, 87])
s1.get_total()

s1.name = "shaban"
s1.get_total() """


#  Static Methods
"""class Student:
    
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def hello():
        print("hello")

s1 = Student("shaban")
s1.hello()"""

#  IMPORTANT
#abstraction (HIDING THE IMPLEMENTATION DETAILS OF A CLASS AND ONLY SHOWING THE ESSENTIAL FEATURES TO THE USER.)
"""class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()"""

#encapsulation  (WRAPPING DATA AND FUNCTIONS INTO A SINGLE UNIT(OBJECT).)


# Q2)  CREATE ACCOUNT CLASS WITH 2 ATTRIBUTES - BALANCE & ACCOUNT N0.
#      CREATE METHODS FOR DEBIT, CREDIT & PRINTING THE BALANCE.
"""class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

        #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

        #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "is credited")
        print("total balance = ", self.get_balance())

        #printing the balance
    def get_balance(self):
        return self.balance
        

acc1 = Account(10000, 12345)
acc1.credit(1000) 
acc1.debit(2000)""" 