def student(name,**details):
    print(name)
    for i,j in details.items():
        print(i,j)

student('abhijeet',age=28,contact=9501487688)
