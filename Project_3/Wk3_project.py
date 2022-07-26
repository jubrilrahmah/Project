print(" Week-3 Project")
# print("Bank account that withdraw and deposit")
# # Create a BankAccount class
# # It should have similar attributes of a conventional bank
# # It should have methods that implement the deposit and withdrawal functionality of a bank account
# # Test that your code is working properly
# # Push your code to github

#This create a method where the deposit and withdraw works intertwined with starting account of 0.
class BankAccount:


    def __init__(self, name, accno):
        self.balance = 0
        self.name = name
        self.acct = accno
        
#Account description containing name and account number
    def des(self):
        print("account created")
        return "Name: {} ; Account no: {}". format(self.name, self.acct)
       

#Returning the current account balance
    def accdes(self):
       
        return"Your Currrent balance is :Acct: {} ; balance: {};". format(self.acct, self.balance)

# creatinga a deposit method
    def deposit(self, creditdes = "Myself"):
        amount = float(input("Amount to deposit: "))
        self.balance = self.balance + amount 
        self.des = creditdes

        print ( "\n Acct:", self.acct,                   
                    "\n Amt:", amount, 
                    "\n CR Desc: from ", creditdes,
                    "\n Available Bal: ", self.balance  )

#creating a withdrawal method
    def withdraw(self, withdrawdes):
        amount = float(input("Amount to withdraw: "))
        self.des = withdrawdes

        if amount <= self.balance:
            self.balance = self.balance - amount
            print("\n Acct:", self.acct, 
                    "\n Amt:", amount,
                    "\n DR Desc: from ", self.name, " To ", self.des,
                    "\n Available Bal: ", self.balance)

        else:
            print("Insufficient funds")
            print("Make a deposit")

    def enquiry(self):
        print("Your balance is: ", self.balance)
           


p = BankAccount(input("Enter your first name and Last name: "), input("input your account no: "))
print("\n", p.des())
print(p.accdes())
print("\n", p.deposit("Damilola"))
print("\n", p.withdraw(input("Enter the name your are sendin to: ")))
print(p.accdes())

print("#..............................................")
print("My second option")
#This deposit and withdrawal method works separately with one account balance, knowing fully well your initial bank balance

class Bank_Account:


    def __init__(self, name, balance, accno):
        self.name = name
        self.accbalance = balance
        self.acct = accno
        
#Account description containing name and account number
    def des(self):
        return "Name: {} ; Account no: {}". format(self.name, self.acct)


#Returning the current account balance
    def accdes(self):
        return"Your Currrent balance is :Acct: {} ; balance: {};". format(self.acct, self.accbalance)


#creating a withdrawal method
    def withdraw(self, amount, withdrawdes):
        self.amt = amount
        self.des = withdrawdes

        if self.amt <= self.accbalance:
            print("\n Acct:", self.acct, 
                    "\n Amt:", self.amt,
                    "\n DR Desc: from ", self.name, " To ", self.des,
                    "\n Available Bal: ", self.accbalance - self.amt)

        else:
            print("Insufficient funds, Your balance is ", self.accbalance)
            print("Make a deposit")
           
# creatinga a deposit method

    def deposit(self, amount, creditdes):
        self.amt = amount
        self.des = creditdes

        print ( "\n Acct:", self.acct,                   
                    "\n Amt:", self.amt, 
                    "\n CR Desc: from ", self.des, " To ", self.name,
                    "\n Available Bal: ", self.accbalance + self.amt )


p = Bank_Account(input("Enter your first name and Last name: "), float(input("Enter your account balance: ")), input("input your account no: "))
print("\n", p.des())
print(p.accdes())
print("withdraw")
print("\n", p.withdraw(float(input("Amount to withdraw: ")), "Damilola"))
print("deposit")
print("\n", p.deposit(float(input("Amount to deposit: ")), "Damilola"))
