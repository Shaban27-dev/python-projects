#   OOPS (PART 2)
#del keyword
"""class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("shaban")

del s1
print(s1)"""

#private(like) attributes & methods
#("PRIVATE ATTRIBUTES & METHODS ARE MEANT TO BE USED ONLY WITHIN THE CLASS AND ARE NOT ACCESSIBLE FROM OUTSIDE THE CLASS")
"""class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass 

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass()) """

"""class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()


p1 = Person()
print(p1.welcome()) #this will print hello bcz it is inside the class
print(p1.__hello()) #this can't print hello bcz it is outside the class."""

# INHERITANCE
#Single inheritance
"""class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.color) """

#Multi-level inheritance
"""class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand= brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("petrol")
print(car1.stop())
print(car1.type)"""

#Multiple inheritance
"""class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)"""

# Super method
"""class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name= name
        super().start()
        

car1 = ToyotaCar("prius", "electric")
print(car1.name)
print(car1.type)"""

#Class method
"""class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     self.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("shaban")
print(p1.name)
print(Person.name) """

# Property  (we use @property decorator on any method in the class to use the method as a property.)
"""class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    # def calc_percentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(98, 87, 80)
print(s1.percentage)

s1.phy = 86
# print(s1.phy)
# s1.calc_percentage()
print(s1.percentage)"""

# Polymorphism : Operator Overloading
# (WHEN THE SAME OPERATOR IS ALLOWED TO HAVE DIFFERENT MEANING ACCORDING TO THE CONTEXT.)
"""class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(3, 5)
num1.showNumber()

num2 = Complex(6, 8)
num2.showNumber()

# sum = num1.add(num2)
# sum.showNumber()

sum = num1 + num2
sum.showNumber()

diff = num1 - num2
diff.showNumber()"""

# Q1)  DEFINE A CIRCLE CLASS TO CREATE A CIRCLE WITH RADIUS R USING THE CONSTRUCTOR.
#      DEFINE AN AREA() METHOD OF THE CLASS WHICH CALCULATES THE AREA OF THE CIRCLE.
#      DEFINE A PERIMETER() METHOD OF THE CLASS WHCIH ALLOWS YOU TO CALCULATE THE PERIMETR OF THE CIRCLE.

"""class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius **2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(8)
print(c1.area())
print(c1.perimeter())"""

#  SAME QUESTION OF SQUARE.
"""class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
    def perimeter(self):
        return 4 * self.side
    
s1 = Square(5)
print(s1.area())
print(s1.perimeter())"""

# Q2)  DEFINE A EMPLOYEE CLASS WITH ATTRIBUTES ROLE, DEPARTMENT & SALARY. THIS CLASS ALSO HAS A SHOWDETAILS() METHOD.
#      CREATE AN ENGINEER CLASS THAT INHERITS PROPERTIES FROM EMPLOYEES & has additional attributes : name & age.
"""class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary 

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("sal =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "90000")

engg1 = Engineer("shaban", 20)
print(engg1.name)
print(engg1.age)
engg1.showDetails()"""

# Q3)  CREATE A CLASS CALLED ORDER WHICH STORES ITEM & ITS PRICE.
#      USE DUNDER FUNCTION__GT__() TO CONVEY THAT:
#          ORDER1 > ORDER2 IF PRICE OF ORDER1 > PRICE OF ORDER2 
"""class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("chips", 20)
odr2 = Order("chocolate", 10)
print(odr1 > odr2)"""
       