# Day 12 — Student Report Card Generator

A Python script that reads student scores from a CSV file, calculates each student's average, assigns a letter grade, and prints a formatted report card table with class statistics.

---

## Features

- Reads student data directly from a CSV file
- Calculates average score per student
- Assigns letter grades (A through F) based on score ranges
- Displays a clean, aligned report card table in the terminal
- Shows total number of students and the overall class average

---

## Concepts used

- File handling — reading and parsing CSV files
- Loops and data processing
- Average calculation and grade assignment logic
- String formatting for tabular output
- Exception handling for missing or invalid data

---

## Requirements

No external libraries required — uses Python's built-in `csv` module.

---

## How to run

1. Add your student data to `students.csv` in the format:

```
Name,Math,Science,English
Alice,85,90,78
Bob,60,55,70
```

2. Run the script:

```bash
python main.py
```

### Example output

```
====== REPORT CARD ======
Name       Avg     Grade
-------------------------
Alice      84.3    B
Bob        61.7    D
-------------------------
Total Students : 2
Class Average  : 73.0
```

---

## Project structure

```
Day_12_Report-Card-Generator/
├── main.py
├── students.csv
└── README.md
```
