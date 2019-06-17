class A:

    def f1(self):
        return 10

class B(A):
    def f2(self):pass



ob=B()
print(ob.f1())
