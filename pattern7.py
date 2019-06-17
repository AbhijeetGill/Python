s=input("enter the string::")
length=len(s)
for row in range(length):
    for col in range(row+1):
        print(s[col],end="")
    print()
