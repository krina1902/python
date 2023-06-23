def oddeven(a):
    if a%2 == 0:
        print(a,"is even number.")
    else:
        print(a,"is odd number.")

def maxtwo(a,b):
    if a>b:
        print(a,"is greater number.")
    else:
        print(b,"is greater number.")


def maxthree(a,b,c):
    if a>b:
        if a>c:
            print(a,"is greater number.")
        else:
            print(c,"is greater number.")
    elif b>c:
        print(b,"is greater number.")
    else:
        print(c,"is greater number.")


def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
               print(n,"is not prime number")
               break
        else:
            print(n,"is prime number")
    else:
        print(n,"is not prime number")


def fibonaaci(n):
    a,b = 0,1

    print(a,end=" ")
    while b<n:
        print(b,end=" ")
        a,b=b,a+b


    
                
       
