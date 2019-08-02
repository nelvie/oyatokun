from random import randint
bankaccount = {}
depositcash = {}
class Bank:
    

    def newaccount(self):
        self.name = input("Enter the account holder name: ")
        self.pin = input("Enter phone no : ")
        self.deposit = int(input("Enter The Initial amount: "))
        self.accountno = randint(1000000,9999999)
        bankaccount[self.name] = self.accountno
        print("Your account no is",self.accountno)
        print("\n\n\nAccount Created")

    def depositAmount(self,amount):
        self.deposit += amount

    
bank = Bank()


while True:
    print("1. CREATE NEW ACCOUNT")
    print("2. DEPOSIT AMOUNT")
    print("Select Your Option (1-2) ")
    choice = int(input("Choose your option:"))

    if choice == 1:
        bank.newaccount()
    elif choice == 2:
        amount = int(input('Enter your account number: '))
        bank.deposit(amount)
            
else:
    print("Invalid ")
