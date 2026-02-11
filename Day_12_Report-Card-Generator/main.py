#          DAY-12
# Student Report Card Generator (read from file, calculate average).
import os

filename = "C:\\Users\\Lenovo\\classroom\\apna college\\100days\\students.csv"

file_content = """Name,Math,Science,English,History
Shaban,91,80,88,83
Sarib,88,79,83,90
James,84,90,93,80
Ethan,90,87,81,80
Harry,85,81,78,79"""

with open(filename, "w")as f:
    f.write(file_content)

print(f"{filename} created successfully!")

def calculate_average(average):
    if average >= 90: return 'A'
    elif average >= 80: return 'B'
    elif average >= 70: return 'C'
    elif average >= 60: return 'D'
    else: return 'F'

def generate_report(file_path):
    print("-" * 65)
    print(f"{'STUDENT NAME':<15} | {'SCORE':<20} | {'AVG':<6} | {'GRADE':<3}")
    print("-" * 65)

    class_total = 0
    student_count = 0

    try:
        with open(filename, "r")as f:
            header = next(f)

            for line in f:
                parts = line.strip().split(',')

                name = parts[0]
                score = [int(value) for value in parts[1:]]
                avg = sum(score) / len(score)

                grade = calculate_average(average=avg)

                class_total += avg
                student_count += 1

                scores_str = ", ".join(map(str, score))
                print(f"{name:<15} | {scores_str:<20} | {avg:<6.1f} | {grade:<3}")

        print("-" * 65)

        if student_count > 0:
            class_avg = class_total / student_count
            print(f"Student count: {student_count}")
            print(f"Class average: {class_avg:.2f}")

    except FileNotFoundError:
        print(f"Error: The file path '{filename}' is not found!")
    except ValueError:
        print("Error: The file contains non numeric content in score columns.")

generate_report(filename)