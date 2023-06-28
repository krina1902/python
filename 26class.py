class Student:

    def getdata(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def putdata(self):
        print("First Name:",self.fname)
        print("Last Name:",self.lname)

s1=Student()
s1.getdata("Krina","Antala")
s1.putdata()
