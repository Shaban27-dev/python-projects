# Day 16 — Smart Calculator (Dictionary-Based)

A command-line calculator that supports seven arithmetic operations through a dictionary-based dispatch system. The result of each calculation can be carried forward into the next, making it easy to chain operations without re-entering numbers.

---

## Features

- Addition, subtraction, multiplication, and division
- Power, modulo, and floor division
- Division-by-zero protection
- Continue calculating using the current result
- Start a new calculation at any point
- Exit option available at every prompt

---

## Concepts used

- Dictionary mapping for operation dispatch
- Functions for modular calculation logic
- Loops for continuous operation
- Conditional statements and error handling
- User input handling

---

## How to run

```bash
python main.py
```

### Example

```
Enter first number: 20
Choose operation (+, -, *, /, **, %, //): *
Enter second number: 3
Result: 60

Continue with 60? (yes/no): yes
Choose operation: **
Enter second number: 2
Result: 3600
```

---

## Project structure

```
Day_16_Smart-Calculator/
├── main.py
└── README.md
```
