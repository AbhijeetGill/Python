n=int(input("enter number of rows::"))
for row in range(0,n):
    for col in range(n,0,-1):
        if col==n-1 or row==n-1 or row+col==4:
            print("*",end="")
    print()
