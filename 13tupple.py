t = ("tops",1,2,2.2,3,45,6,True,[600,200,900,400],"string:")

print(t)
print(t.count(1))
print(t.index(2.2))

for i in t:
    print(i)

t[8].append(1)
print(t)
t[8].sort()
print(t)

print(10 in t)
print(1 in t)
