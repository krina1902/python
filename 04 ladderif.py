#marksheet
roll=int(input("enter roll no:"))
name=input("enter student name:")
s1=int(input("enter the mark of maths:"))
s2=int(input("enter the mark of physics:"))
s3=int(input("enter the mark of chemistry:"))
total=s1+s2+s3
per=total/3
print("Total marks:",total)
print("Percantage:",per)

if per>=70:
    print("Distiction!!")
elif per>=60:
    print("First class")
elif per>=50:
    print("Second class")
elif per>=35:
    print("third class")
else:
    print("Fail")
    
       
