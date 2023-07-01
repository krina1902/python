class A:
    def show(self):
        print("show A")
class B(A):
    def show(self):
        super().show()
        print("show B")
class C(B):
    def show(self):
        super().show()
        print("show C")
class D(C):
    def show(self):
        super().show()
        print("show D")

d1=D()
d1.show()
