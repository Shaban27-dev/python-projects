#          DAY-20
# CSV Report Generator
# Read marks
# Generate grade sheet
# Save new CSV
import pandas as pd

# File paths
input_path = r"C:\Users\Lenovo\classroom\apna college\100days\students.csv"
output_path = r"C:\Users\Lenovo\classroom\apna college\100days\students_with_grades.csv"

# Read CSV
data = pd.read_csv(input_path)

# Clean column names (removes extra spaces)
data.columns = data.columns.str.strip()

# Convert marks to numeric (handles text or empty values safely)
data["marks"] = pd.to_numeric(data["marks"], errors="coerce")

# Grade function
def calculate_grade(marks):
    if pd.isna(marks):
        return "Absent"
    elif marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'Fail'

# Create Grade column
data["Grade"] = data["marks"].apply(calculate_grade)

# Class statistics
class_average = data["marks"].mean()
topper_name = data.loc[data["marks"].idxmax(), "name"]
num_failures = (data["Grade"] == "Fail").sum()

# Grade distribution
grade_distribution = data["Grade"].value_counts()

# Print report
print("----- Student Report -----\n")
print(data)

print("\nClass Average:", round(class_average, 2))
print("Topper Name:", topper_name)
print("Number of Failures:", num_failures)

print("\nGrade Distribution:")
print(grade_distribution)

# Save new CSV
data.to_csv(output_path, index=False)

print("\nGrade sheet generated successfully")
print("Saved at:", output_path)