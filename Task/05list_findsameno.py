l=[1,2,3,4,2,3,5,56,78,78,90,"tops","tops"]
l1=[]

for i in l:
    if i not in l1 and l.count(i)>1:
        l1.append(i)
print(l1)
