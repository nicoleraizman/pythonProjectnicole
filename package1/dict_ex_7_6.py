dic1={1:10,2:20,3:30,4:40,5:50}


key = int(input("enter key: "))
if key in dic1:
    del dic1[key]

print(dic1)


