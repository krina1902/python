s = ["123",456,1.2,"tops",1.1,"python",True,False]

print(len(s))
s.append(100)
print(s)
s1=s.copy()
print(s1)
s2=s1
s2.append(900)
print(s2)
print(s1)
print(s)
#s.extend(s1)
#print(s)
s.reverse()
print(s)
print(s.count(1))
print(s.index(1.2))
s.insert(1,451)
print(s)
