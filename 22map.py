def multiplication (y):
    return y*y

no=(22,33,44,55,66,77)
mul=map(multiplication,no)
print(list(mul))

def add(a,b):
    return a+b

a=(1,2,3,4,5,6,7)
b=(1,2,3,4,5,6,7)
addition=map(add,a,b)
print(list(addition))
