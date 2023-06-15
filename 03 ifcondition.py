'''
simple if


a=int(input("enter your age"))
if a>18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

a = int(input("enter number:"))
if a%2==0:
    print("a is even number")
else:
    print("a is odd number")
'''
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>b:
    if a>c:
        print("a is large",a)
    else:
         print("c is large",c)
elif b>c:
    print("b is large",b)
else:
     print("c is large",c)

