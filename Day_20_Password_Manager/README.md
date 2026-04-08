# Day 20 — Password Manager (Tkinter GUI)

A desktop password manager built using Python and Tkinter that allows users to generate strong passwords, store credentials securely in a JSON file, and retrieve saved login details instantly.

---

## Features

- Generate strong random passwords (letters, numbers, symbols)
- Automatically copies generated password to clipboard
- Save website credentials (email + password) to a JSON file
- Search and retrieve saved credentials instantly
- Handles missing or empty data files safely
- Simple and clean GUI using Tkinter

---

## Concepts used

- `tkinter` — GUI development (labels, buttons, entry fields, messagebox)
- json — storing and retrieving structured data
- random — password generation logic
- File handling — read/write JSON data
- Exception handling — FileNotFoundError, JSONDecodeError
- Clipboard handling using `pyperclip`

---

## Requirements

```bash
pip install pyperclip
```

---

## How to run

```bash
python main.py
```

## How it works

```
Enter the website name and email/username
Click Generate Password (optional)
Click Add to save credentials
Use Search to retrieve saved data
Example
Website: google.com
Email: test@gmail.com
Password: Xy@9#Lm2Pq

Saved successfully!

Search → google.com

Email: test@gmail.com
Password: Xy@9#Lm2Pq
```

---

## Project structure

```
Day_20_Password_Manager/
├── main.py
├── data.json
├── logo.png
└── README.md
```
