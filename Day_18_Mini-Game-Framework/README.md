# Day 18 — Mini Game Framework (OOP)

A menu-driven game launcher built with object-oriented programming. A reusable base `Game` class provides shared logic — score tracking, menus, and end screens — and three child games inherit from it.

---

## Features

- Menu-based launcher to select and start any game
- Base `Game` class with shared score tracking and session management
- Three built-in mini games (see below)
- Replay any game without returning to the launcher
- Clean inheritance structure — easy to extend with new games

---

## Games included

### Guess the Number
- Computer picks a random number between 0 and 20
- Player keeps guessing until correct
- Counts attempts per round

### Quiz Game
- Randomly selects 5 questions from a question bank
- Tracks score and shows percentage at the end

### Rock Paper Scissors
- Player vs computer
- First to 5 wins is declared the champion

---

## Concepts used

- Object-oriented programming — inheritance, base and child classes
- Lists and dictionaries for question and game data
- `random` module for number generation and question selection
- Loops and conditionals for game logic
- User input handling

---

## How to run

```bash
python main.py
```

### Example

```
===== Mini Game Launcher =====
1. Guess the Number
2. Quiz Game
3. Rock Paper Scissors
4. Exit

Select a game: 2

Q1: What is the largest planet in the solar system?
Your answer: Jupiter
Correct!
...
Final Score: 4/5 (80%)
```

---

## Project structure

```
Day_18_Mini-Game-Framework/
├── main.py
└── README.md
```
