n=int(input("enter number of terms::"))
c=n
for row in range(0,n):
    for col in range(0,c):
        print("*",end="")
    c=c-1
    print()