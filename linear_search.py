n=int(input("enter number  to find:"))
a=[1,2,3,4,5,6,7]
b=iter(a)
i=0
for i in range(len(a)):
    c=next(b)
    if n==c:
        print("number found")
        break
else:
    print("not found")