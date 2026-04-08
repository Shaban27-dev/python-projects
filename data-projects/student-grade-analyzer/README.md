# Day 19 — Student Grade Analyzer (Pandas)

A data analysis script that reads student marks from a CSV file, cleans the data, calculates grades, and generates a detailed class performance report using the Pandas library.

---

## Features

- Reads student data from a CSV file
- Cleans column names and handles missing or invalid mark entries
- Automatically assigns letter grades based on score thresholds
- Calculates the overall class average
- Identifies the top-scoring student
- Counts the number of students who failed
- Displays a grade distribution summary
- Saves the updated grade sheet to a new CSV file

---

## Concepts used

- `pandas` library — DataFrames, filtering, and aggregation
- CSV file handling — read and write
- Data cleaning — handling nulls and invalid values
- Grading logic with `apply()` functions
- Statistical functions — mean, value counts

---

## Requirements

```bash
pip install pandas
```

---

## How to run

1. Add your student data to `students.csv` in the format:

```
Name,Marks
Alice,88
Bob,45
Charlie,72
```

2. Run the script:

```bash
python main.py
```

### Example output

```
===== Class Performance Report =====
Class Average : 68.3
Topper        : Alice (88)
Failed Students: 1

Grade Distribution:
A    1
C    1
F    1

Updated grade sheet saved to: grades_output.csv
```

---

## Project structure

```
Day_19_Student-Grade-Analyzer/
├── main.py
├── students.csv
├── grades_output.csv
└── README.md
```
