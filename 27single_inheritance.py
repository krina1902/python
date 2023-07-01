class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A: ",self.a)

class B(A):
     def getB(self,b):
        self.b=b
     def putB(self):
        print("B: ",self.b)

a1=B()
a1.getA(10)
a1.putA()
a1.getB(20)
a1.putB()
