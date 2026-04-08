# Day 06 — Hangman Game

A classic Hangman game played in the terminal. The computer picks a random word and the player guesses it letter by letter before running out of lives.

---

## Features

- Random word selected from a built-in word bank
- 6 lives total — one lost per incorrect guess
- ASCII art hangman updated after each wrong guess
- Prevents duplicate letter guesses
- Win or lose ending with the correct word revealed

---

## Concepts used

- Loops and conditionals
- Lists and strings
- `random` module
- User input handling

---

## How to run

```bash
python main.py
```

### Example

```
_ _ _ _ _ _   (6 lives remaining)
Guess a letter: e
Good guess!

_ e _ _ _ _   (6 lives remaining)
Guess a letter: z
Wrong! 

_ e _ _ _ _   (5 lives remaining)
```

---

## Project structure

```
Day_06_Hangman-Game/
├── main.py
└── README.md
```
