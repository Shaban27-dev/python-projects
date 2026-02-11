#          DAY_4
# Simple ATM simulator(Deposit, Withdraw, Balance).
balance = 10000

def check_balance():
    print(f"Your current balance is ${balance:.2f}")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} deposited succesfully.")
    else:
        print("Invalid deposit amount")

def withdraw(amount):
    global balance
    if amount <= balance and amount > 0:
        balance -= amount
        print(f"${amount:.2f} withdrawn successfully!")
        check_balance()
    elif amount > balance:
        print("Insufficient funds!")
    else:
        print("Invalid withdrawal amount!")

def atm():
    while True:
        ask = input("what do you want to do? ('Deposit', 'Withdraw', 'check_balance' or 'exit'): ").lower()
        if ask == "exit":
            print("Thanks for using ATM, GOODBYE!")
            break
        if ask == "check_balance":
            check_balance()
        elif ask == "deposit":
            amt = float(input("How much amount do you want to deposit: "))
            deposit(amt)
        elif ask == "withdraw":
            amt = float(input("How much amount do you want to withdraw: "))
            withdraw(amt)
        else:
            print("Invalid choice!")

atm()