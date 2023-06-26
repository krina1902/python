print("#"*70)

try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b
    print("Division:",c)

    index=[1,2,3,4,5,6]
    print(index[9])
  
##except ZeroDivisionError as e:
##    print("Exception caught",e)
##except ValueError as e:
##    print("Exception caught",e)
##except IndexError as e:
##    print("Exception caught",e)


except Exception as e:
    print("Exception caught",e)
finally:
    print("Finally called.....")
print("#"*70)
