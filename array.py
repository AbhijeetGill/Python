import array
arr=array.array('i',[])
for i in range(5):
    x=int(input("enter value:"))
    arr.append(x)
print(arr)
num=array(arr.typecode,(a for a in arr))
