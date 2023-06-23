import random


data=open("11data.txt","w")
for i in range(10):
    num = random.randint(1,100)
    data.write(str(num)+",")
data.close()

data=open("11data.txt","r")
even=open("12even.txt","w")
odd=open("13odd.txt","w")
l=data.read().split(",")[:-1]
print(l)

for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
data.close()
even.close()
odd.close()


print("Data file content")
data=open("11data.txt","r")
print(data.read())
data.close()

print("Even file content")
even=open("12even.txt","r")
print(even.read())
even.close()

print("Odd file content")
odd=open("13odd.txt","r")
print(odd.read())
odd.close()
