#function with no argument and no return:

def printstar():
    print("*"*50)

printstar()
print("Python Programming")
printstar()

#function with argument and no return:

def Addition(a,b):
    print("Addtion of two values:",a+b)

Addition(3,4)
x=int(input("Enter x:"))
y=int(input("Enter y:"))
Addition(x,y)
printstar()

#function with argument and return:

def modulo(a,b):
    return a%b

printstar()
print("Modulo:",modulo(25,4))
