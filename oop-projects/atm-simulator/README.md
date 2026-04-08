# Day 04 — ATM Simulator

A command-line ATM simulation with PIN authentication, balance checking, deposit, and withdrawal functionality.

---

## Features

- PIN-based login with limited retry attempts
- Deposit money into the account
- Withdraw money with insufficient-funds protection
- Check current balance
- Displays a transaction summary after each operation

---

## Concepts used

- Loops and conditionals
- Functions
- Variables for state management
- Input validation and error handling

---

## How to run

```bash
python main.py
```

### Example

```
Enter PIN: ****
Welcome!

1. Deposit
2. Withdraw
3. Check Balance
4. Exit

Select option: 2
Enter withdrawal amount: 500
Transaction successful. Remaining balance: $1500.00
```

---

## Project structure

```
Day_04_ATM-Simulator/
├── main.py
└── README.md
```
