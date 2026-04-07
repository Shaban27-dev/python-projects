# Day 03 — Number Guessing Game

A command-line guessing game where the computer picks a random number and the player tries to guess it within a limited number of attempts.

---

## Features

- Three difficulty modes: Easy, Medium, and Hard
- Limited attempts per difficulty level
- Higher / lower hints after each wrong guess
- Tracks best score (fewest attempts) and worst score across sessions

---

## Concepts used

- Loops (`while`)
- Functions
- `random` module
- Conditional statements
- Score tracking with variables

---

## How to run

```bash
python main.py
```

### Example

```
Choose difficulty — Easy (10 attempts) / Medium (7) / Hard (5): Medium
Guess the number (1–100): 50
Too high! Try again.
Guess the number (1–100): 30
Too low! Try again.
Guess the number (1–100): 42
Correct! You got it in 3 attempts.
```

---

## Project structure

```
Day_03_Number-Guessing-Game/
├── main.py
└── README.md
```
