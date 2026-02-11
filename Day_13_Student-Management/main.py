#          DAY-13
# Write a program for a Student Management System
# Add student
# Remove student
# Update student marks
# Print details
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks    
    
    def update_marks(self, new_marks):
        self.marks = new_marks

    def __str__(self):
        return f"Roll No : {self.roll_no} | Name: {self.name} | Marks: {self.marks}"
        

students = []

while True:
    print("\n---- Student Management System ----")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student Marks")
    print("4. View Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = int(input("Enter roll number: "))
        marks = int(input("Enter marks: "))

        for s in students:
            if s.roll_no == roll_no:
                print("Student with this roll number already exists!")
                break
        else:
            student = Student(name, roll_no, marks)
            students.append(student)
            print("Student added successfully!")

    elif choice == "2":
        roll_no = int(input("Enter roll number to remove: "))
        for s in students:
            if s.roll_no == roll_no:
                students.remove(s)
                print("Student removed successfully!")
                break
        else:
            print("Student not found!")

    elif choice == "3":
        roll_no = int(input("Enter roll number to update marks: "))
        for s in students:
            if s.roll_no == roll_no:
                new_marks = int(input("Enter new marks: "))
                s.update_marks(new_marks)
                print("Marks updated successfully!")
                break
        else:
            print("Student not found!")

    elif choice == "4":
        if not students:
            print("No student found!")
        else:
            print("\nStudent List: ")
            for s in students:
                print(s)

    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Please make a valid choice.")