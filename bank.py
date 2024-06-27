class Bank:
    def __init__(self, acc_no, acc_bal, age, name):
        self.acc_no = acc_no
        self.acc_bal = acc_bal
        self.age = age
        self.name = name
    
    def deposit(self, deposit_amount):
        self.acc_bal += deposit_amount
        print("Account balance:", self.acc_bal)
    
if __name__ == "__main__":
    name = input("Enter name: ")
    print("Enter age:")
    age = int(input())
    print("Enter the account number:")
    acc_no = int(input())
    
    b = Bank(acc_no, 100, age, name)
    
    print("Enter the amount to be deposited:")
    deposit_amt = int(input())
    b.deposit(deposit_amt)
