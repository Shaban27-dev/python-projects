# Day 05 — To-Do List

A command-line task manager that lets you add, view, and remove tasks. Tasks are stored persistently so they survive between sessions.

---

## Features

- Add new tasks
- View all current tasks with their status
- Remove tasks by number
- Persistent storage — tasks are saved to a file and reloaded on next run

---

## Concepts used

- Lists and dictionaries
- Loops and functions
- File handling for persistence
- Error handling for invalid input

---

## How to run

```bash
python main.py
```

### Example

```
1. Add Task
2. View Tasks
3. Remove Task
4. Exit

Select option: 1
Enter task: Buy groceries
Task added!

Select option: 2
1. [ ] Buy groceries
```

---

## Project structure

```
Day_05_ToDo-List/
├── main.py
├── tasks.json
└── README.md
```
