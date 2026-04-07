# Day 17 — Modified Snake Game

A modified version of the classic Snake game built with Python Turtle. This version adds speed control, snake and background color customization, and a pause/resume toggle on top of the standard gameplay.

---

## Features

- Classic snake movement using arrow keys
- Change the snake's color — Red, Green, or Blue
- Random snake color mode
- Switch background colors with number keys
- Speed up or slow down the snake during gameplay
- Pause and resume at any time
- Wall collision detection — game ends on contact

---

## Concepts used

- `turtle` module for rendering
- Keyboard event handling with `onkey()` and `listen()`
- `time` module for delay-based speed control
- Loops and conditionals for game logic
- `random` module for random color mode
- Collision detection with coordinate comparison

---

## Requirements

No external libraries — uses Python's built-in `turtle` and `time` modules.

---

## How to run

```bash
python main.py
```

A Turtle graphics window opens. Use the controls below to play.

---

## Controls

| Key | Action |
|-----|--------|
| Arrow keys | Move the snake |
| `r` | Red snake |
| `g` | Green snake |
| `b` | Blue snake |
| `x` | Random snake color |
| `1` / `2` / `3` | Change background color |
| `+` | Speed up |
| `-` | Slow down |
| `p` | Pause / Resume |

---

## Project structure

```
Day_17_Modified-Snake-Game/
├── main.py
└── README.md
```
