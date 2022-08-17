num=""
total=0
count=0

for i in range(6):
    num=int(input("enter number: "))
    total+=num
    count+=1

print("total",total)
print("avg",total/count)