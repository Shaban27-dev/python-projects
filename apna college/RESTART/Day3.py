#  LISTS IN PYTHON      list = mutable(can change)
"""marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])"""

"""student = ["shaban", 87.4, 20, "odisha"]
student[0] = "sarib"
print(student)"""

#  LIST SLICING
"""marks = [87, 64, 33, 95, 76]
marks[1:4]
marks[ :4]
marks[1: ]
print(marks[-3:-1])"""

#   LIST METHODS
"""list = [2, 1, 3]

list.append(4)  #adds one element at the end  [2,1,3,4]
list.sort()  #sorts in ascending order  [1,2,3]
list.sort(reverse=True)  #sorts in descending order  [3,2,1]
list.reverse()  #reverses list  [3,1,2]
list.insert(2, 4)  #insert element at index  [2,1,4,3]
list.remove(1)  #removes first occurrence of element  [2,3]
list.pop(0)  #removes element at idx"""

#   TUPLES IN PYTHON      TUPLES = IMMUTABLE(CAN'T CHANGE)
"""tup = (2, 1, 3, 1)
print(tup[0])
print(tup[1])"""

#   TUPLE METHODS
"""tup = (2, 1, 3, 1)
tup.index(el)  #removes index of first occurrence  tup.index(1) is 1
tup.count(el)  #counts total occurrences  tup.count(1) is 2"""

#  Q1)  WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVORITE MOVIES & STORE THEM IN A LIST.
"""a = input("enter 1st movie :")
b = input("enter 2nd movie :")
c = input("enter 3rd movie :")

list = [a, b, c]
print(list)"""

#  Q2)  WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS.(HINT:USE COPY()METHOD)
#       [1,2,3,2,1]     [1,"ABC", "ABC", 1]
"""list = ["a", "b", "c", "b", "a"]
copied_list = list.copy()
copied_list.reverse()
if(list == copied_list):
    print("this is palindrome")
else:
    print("this is not palindrome")"""

#  Q3)  WAP TO COUNT THE NUMBER OF STUDENTS WITH THE "A" GRADE IN THE FOLLOWING TUPLE.
#       ["C", "D", "A", "A", "B", "B", "A"]
"""tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))"""

#  Q4)  STORE THE ABOVE VALUES IN A LIST & SORT THEM FROM "A" TO "D"
"""grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)"""