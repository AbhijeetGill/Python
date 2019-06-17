def B(list):
   for i in list:
     yield i
a=[1,2,3,4,5]
x=B(a)
print(next(x))

