class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B:
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)

class C(A,B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)

a1=C()
a1.getA(10)
a1.getB(20)
a1.getC(30)
a1.putA()
a1.putB()
a1.putC()
