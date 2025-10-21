          
#    File. I\O
"""f = open("apna college\\RESTART\\demo.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()"""

"""f = open("apna college\\RESTART\\demo.txt", "a")

f.write("\nAnd then i'll learn reactjs")

f.close()"""

"""with open("apna college\\RESTART\\demo.txt", "r") as f:
    data = f.read()
    print(data)


with open("apna college\\RESTART\\demo.txt", "w") as f:
    f.write("new data")"""

# import os
# os.remove("any file name")

# Q1)  CREATE A NEW FILE "PRACTICE.TXT" USING PYTHON. ADD THE FOLLOWING DATA IN IT:
# HI EVERYONE
# WE ARE LEARNING FILE I/O
# USING JAVA
# I LIKE PROGRAMMING IN JAVA

"""f = open("apna college\RESTART\practice.txt", "a")
f.write("i like programming in java")
f.write("\ncurrently learning python")
f.close"""

"""with open("apna college\RESTART\practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning file I/O\n")
    f.write("using java.\nI like programming in java.")"""

# Q2)  WAF THAT REPLACE ALL OCCURRENCES OF "JAVA" WITH "PYTHON" IN ABOVE FILE.
"""with open("apna college\RESTART\practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)

with open("apna college\RESTART\practice.txt", "w") as f:
    f.write(new_data)"""

# Q3)  SEARCH IF THE WORD "LEARNING" EXISTS IN THE FILE OR NOT.
"""word = "learning"
with open("apna college\RESTART\practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != 1):
        print("Found")
    else:
        print("not found")"""

"""def check_for_word():
    word = "learning"
    with open("apna college\RESTART\practice.txt", "r") as f:
        data = f.read()
    if(data.find(word) != 1):
        print("Found")
    else:
        print("not found")

check_for_word()"""

# Q4)  WAF TO FIND IN WHICH LINE OF THE FILE DOES THE WORD "LEARNING" OCCUR FIRST.
#      PRINT -1 IF WORD NOT FOUND.  
"""def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("apna college\RESTART\practice.txt", "r")as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
print(check_for_line())"""

# Q5)  FROM A FILE CONTAINING NUMBERS SEPARATED BY COMMA, PRINT THE COUNT OF EVEN NUMBERS.
"""count = 0
with open("apna college\RESTART\practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)""" 
 
file_path = "C:\\Users\\Lenovo\\classroom\\data.txt"
with open(file_path, mode="r")as f:
    content = f.read()
    print(content.upper())