class A:
    def __init__(self,list):
        self.list=list
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        return self.list[self.index]

a=[1,2,3,4,5]
ob=A(a)
it=iter(ob)
print(next(it))
