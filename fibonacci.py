a=0
b=1
num=int(input("enter no. of terms in fibonacci series:"))
i=1
while i<=num:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1