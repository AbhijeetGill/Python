n=int(input("enter number of terms:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==(n-1) or row==col:
            print("*",end="")
        else:
            print(end=" ")
    print()