class Person:
    def details1(self,name,idno):
        self.name=name
        self.idno=idno
    def display1(self):
        print("Name of employee:",self.name)
        print("Id number of employee:",self.idno)
class E1(Person):
    def details2(self,age,dob):
        self.age=age
        self.dob=dob
    def display2(self):
        print("Age of employee:",self.age)
        print("Date of birth of employee:",self.dob)
class E2(Person):
    def details3(self,salary,post):
        self.salary=salary
        self.post=post
    def display3(self):
        print("Salary of employee:",self.salary)
        print("Post of employee:",self.post)

class E3(E1,E2):
    def details4(self,gender):
        self.gender=gender
    def display4(self):
        print("Gender of employee:",self.gender)

c=E3()
c.details1("Krina",2)
c.details2(24,"19-02-1998")
c.display1()
c.display2()

c.details3(50000,"Intern")
c.display3()

c.details4("Female")
c.display4()
