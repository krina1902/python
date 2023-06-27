product=["ring","necklace","braclete","tikka"]
price=[2345,4569,4567,2134,678]

lis={product:price for product,price in zip(product,price)}
print((lis))

name=["krina","dhruvin","harsukh","hema"]
roll_no=[1,4,3,2]

student={name:roll_no for name,roll_no in zip(name,roll_no)}
print(student)
