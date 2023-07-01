class bank:
    def accountdetail(self,cname,accno,actype):
        self.cname=cname
        self.a=accno
        self.t=actype

    def display(self):
        print("Customer name is:",self.cname)
        print("your account number is:",self.a)
        print("your account type is:",self.t)



cname=input(("Enter customer name: "))
accno=int(input("Enter qccount no: "))



b1=bank()
print("1.Saving")
print("2.Current")
print("3.NRI")
choice=int(input("Enter your choice:"))
if choice==1:
    actype="saving"
elif choice==2:
    actype="current"
elif choice==3:
    actype="NRI"

b1.accountdetail(cname,accno,actype)
b1.display()
