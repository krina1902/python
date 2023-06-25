primef=open("15primef.txt","w")
for i in range(1,101):
   primef.write(str(i)+",")
primef.close()

primef=open("15primef.txt","r")
noprime=open("16noprime.txt","w")
prime=open("17prime.txt","w")
l = primef.read().split(",")[:-1]
print(l)


if int(l)%2!=0:
   for i in range (3,int(l/2)+1,2):
      if int(l)%i==0:
         noprime.write(i+",")
      else:
         prime.write(i+",")
   else:
      noprime.write(i+",")

primef.close()
noprime.close()
prime.close()
