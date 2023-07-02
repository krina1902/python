class person:
    def detail1(self,name,idno):
        self.name=name
        self.idno=idno
class Employee(person):
    def detail2(self,salary,post):
        self.salary=salary
        self.post=post
    def display1(self):
        print(self.name,self.idno,self.salary,self.post)
class employee1(person):
    def detail3(self,age,dob):
        self.age=age
        self.dob=dob
    def display(self):
        print(self.name,self.idno,self.age,self.dob)
class employee12(Employee,employee1):
    def detail4(self,gender):
        self.gender=gender
    def display3(self):
        print(self.name,self.idno,self.gender)




c=employee12()
c.detail3(24,"19-02-1998")
c.detail2(50000,"intern")
c.detail4("female")
c.detail1("krina",23)
c.display3()
c.display()
c.display1()
