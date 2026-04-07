# Day 15 — Simple Drawing App (Turtle)

An interactive drawing application built with Python's Turtle module. Control the turtle with your keyboard to draw freely, switch colors, resize the brush, and clear the canvas.

---

## Features

- Move the turtle in all four directions using arrow keys
- Lift or lower the pen to draw or reposition freely
- Switch between Red, Green, and Blue pen colors
- Enable random color mode
- Increase or decrease brush size
- Clear the canvas and reset the turtle's position

---

## Concepts used

- `turtle` module for graphics and drawing
- Keyboard event handling with `onkey()` and `listen()`
- Functions for each control action
- `random` module for random color generation
- Conditionals for mode switching

---

## Requirements

No external libraries — uses Python's built-in `turtle` module.

---

## How to run

```bash
python main.py
```

A Turtle graphics window opens. Use the controls below to draw.

---

## Controls

| Key | Action |
|-----|--------|
| Arrow keys | Move turtle (forward / backward / turn) |
| `u` | Pen up — move without drawing |
| `p` | Pen down — resume drawing |
| `r` | Red pen color |
| `g` | Green pen color |
| `b` | Blue pen color |
| `x` | Random pen color |
| `+` | Increase brush size |
| `-` | Decrease brush size |
| `c` | Clear the canvas |
| `Space` | Reset turtle to center |

---

## Project structure

```
Day_15_Turtle-Drawing-App/
├── main.py
└── README.md
```
