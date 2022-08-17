num=int(input("enter number: "))
total=0
total1=0
count=0
count1=0

while 0<=num<=100:
    if 60<=num:
        total+=num
        count+=1

    else:
        total1+=num
        count1+=1

    num = int(input("enter number: "))

print(total/count)
print(total1/count1)