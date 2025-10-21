#   DICTIONARY IN PYTHON
"""dict = {
    "name" : "shaban",
    "cgpa" : 9.1,
    "marks" : [98, 97, 95],
}

dict["name"] = "sarib"
dict["surname"] = "alam"
print(dict)"""

"""null_dict = {}
null_dict["name"] = "shaban"
print(null_dict)"""

#   NESTED DICTIONARIES
"""student = {
    "name" : "shaban",
    "subject" : {
        "phy" : 97,
        "chem" : 88,
        "math" : 79,
    }
}
print(student["subject"]["math"])"""

#   DICTIONARY METHODS
"""mydict.keys()  #returns all keys
mydict.values()  #returns all values
mydict.items()  #returns all(key,val)pairs as tuples
mydict.get("key")  #returns the key according to value 
mydict.update(newdict)  #inserts the specified items to the dictionary"""

#   SETS IN PYTHON
"""collection = {1, 2, 3, 4,}

print(collection)
print(len(collection))

collection = set()

print(type(collection))"""

#   SET METHODS
"""set.add(el)  #adds an element
set.remove(el)  #removes the element
set.clear()  #empties the set
set.pop()  #removes a random value
set.union(set2)  #combines both set values & returns new
set.intersection(set2)  #combines common values & returns new"""

#  Q1)  STORE FOLLOWING WORD MEANINGS IN A PYTHON DICTIONARY:
#       TABLE : "A PIECE OF FURNITURE", "LIST OF FACTS & FIGURES"
#       CAT : "A SMALL ANIMAL"
"""meanings = {
    "table" : ("a piece of furniture", "list of facts & figures"),
    "cat" : "a small animal"
}
print(meanings)"""

#  Q2)  YOU ARE GIVEN A LIST OF SUBJECTS FOR STUDENTS. ASSUME ONE CLASSROOM IS REQUIRED FOR 1 SUBJECT.
#       HOW MANY CLASSROOMS ARE NEEDED BU ALL STUDENTS.
#  "PYTHON", {"JAVA", "C++", "PYTHON", "JAVASCRIPT", "JAVA", "PYTHON", "JAVA", "C++", "C"
"""subjects ={"PYTHON", "JAVA", "C++", "PYTHON", "JAVASCRIPT", "JAVA", "PYTHON", "JAVA", "C++", "C"}
print(len(subjects)) 
print(type(subjects))"""

#  Q3)  WAP TO ENTER MARKS OF 3 SUBJECTS FROM THE USER AND STORE THEM IN A DICTIONARY. START WITH AN EMPTY DICTIONARY & ADD ONE BY ONE
#       USE SUBJECT AS KEY & MARKS AS VALUES.
"""null_dict = {}
null_dict["phy"] = 89
null_dict["chem"] = 85
null_dict["math"] = 81
print(null_dict)"""

#  Q4)  FIGURE OUT A WAY TO STORE 9 & 9.0 AS SEPARATE VALUES IN THE SET.
#    (YOU CAN TAKE HELP OF BUILT-IN DATE TYPES)
"""dict = {
    "int" : 9,
    "float" : 9.0
}
print(dict)"""