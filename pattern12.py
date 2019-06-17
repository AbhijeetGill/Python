n=int(input("enter number of rows::"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    for j in range(i):
        print("*",end="")
    print()
