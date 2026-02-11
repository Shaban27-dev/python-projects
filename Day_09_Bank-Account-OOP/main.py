#          DAY-9
# Bank Account OOP Project (deposit, withdraw, balance).
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
          
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Rs:", amount, "is deposited successfully.")
            print("Total balance: ", self.get_balance())
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Rs:", amount, "is withdrawn successfully.")
            print(f"Total balance: ", self.get_balance())
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance
    
acc_1 = Account(10000, 23451)

ask = input("What do you want to do? 'Deposit' or 'Withdraw': ").lower()
if ask == "deposit":
    money = int(input("How much amount do you want to deposit? "))
    acc_1.deposit(money)
elif ask == "withdraw":
    money = int(input("How much amount do you want to withdraw? "))
    acc_1.withdraw(money)
else:
    print("You typed an invalid input!")