import UDF

while True:
    print("1. oddeven")
    print("2. maxtwo")
    print("3. maxthree")
    print("4. prime")
    print("5. fibonaaci")
    print("6.exit")

    choice = int(input("Enter a choice:"))
    print("*"*70)

    if choice==1:
        x=int(input("Enter x:"))
        UDF.oddeven(x)
        print("*"*70)
    elif choice==2:
        a=int(input("Enter a:"))
        b=int(input("Enter b:"))
        UDF.maxtwo(a,b)
        print("*"*70)
    elif choice==3:
        a=int(input("Enter a:"))
        b=int(input("Enter b:"))
        c=int(input("Enter c:"))
        UDF.maxthree(a,b,c)
        print("*"*70)
    elif choice==4:
        x=int(input("Enter x:"))
        UDF.prime(x)
        print("*"*70)
    elif choice==5:
        x=int(input("Enter x:"))
        UDF.fibonaaci(x)
        print("*"*70)
    elif choice==6:
        print("Thank you for visit!!!!")
        break
    else:
        print("Invalid choice. Better luck next time.")
        
        
