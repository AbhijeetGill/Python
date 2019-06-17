def A():
    def B():
        print("inner function")
    return B #closure

a=A()
print(a())