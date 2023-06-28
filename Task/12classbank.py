class Bank:
    def openaccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello,",self.cname,"your account no is ",self.acno,"and your balance is ",self.balance, "rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            self.needs=amount-self.balance
            print("Sorry,you need",self.needs ," for withdraw money.")
    def checkbalance(self):
        print("Your Current Balance is: ",self.balance)
b1=Bank()

cname=input("Enter customer name:")
acno=int(input("Enter account number:"))
balance=int(input("Enter balance:"))

b1.openaccount(cname,acno,balance)
while True:
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    print("#"*70)

    if choice==1:
        amount=int(input("Enter your deposit amount: "))
        b1.deposit(amount)
    elif choice==2:
        amount=int(input("Enter your withdraw amount: "))
        b1.withdraw(amount)
    elif choice==3:
        b1.checkbalance()
    elif choice==4:
        print("Thank you for using our services")
        break
    else:
        print("Invalid choice....")
        
        
    
