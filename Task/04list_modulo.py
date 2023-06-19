l=[]
start=100
end=400

for i in range(start,end):
    if i%5!=0 and i%7==0:
        l.append(i)
print(l)
