#method overloading is not support in python
'''
class A:
    def test(self):
        print("test is without argument")
    def test(self,a):
        self.a=a
        print("test is with a argument")
    def test(self,b):
        self.b=b
        print("test is with b argument")

a1=A()
a1.test()
'''

#magic method

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("init called")
    def __str__(self):
        print("str called")
        return "[{0},{1}]".format(self.x,self.y)
    def __add__(self,obj):
        x=self.x+obj.x
        y=self.y+obj.y
        return point(x,y)


p1=point(10,20)
print(p1)
p2=point(40,30)
print(p2)
print(p1+p2)
