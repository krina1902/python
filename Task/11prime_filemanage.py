primef=open("15primef.txt","w")
for i in range(1,101):
   primef.write(str(i)+",")
primef.close()

primef=open("15primef.txt","r")
noprime=open("16noprime.txt","w")
prime=open("17prime.txt","w")
l = primef.read().split(",")[:-1]
#print(l)

for i in l:
    if int(i)%2==0:
        noprime.write(i+",")
    else:
        for j in range(3,int(int(i)/2)+1,2):
            if int(i)%j==0:
                noprime.write(i+",")
                break
        else:
            prime.write(i+",")

print("*"*50,"Range content","*"*50)
primef=open("15primef.txt","r")
print(primef.read())

print("*"*50,"No prime number in range","*"*50)
noprime=open("16noprime.txt","r")
print(noprime.read())

print("*"*50,"Prime number in range","*"*50)
prime=open("17prime.txt","r")
print(prime.read())



primef.close()
noprime.close()
prime.close()
