num=int(input("enter number: "))
total=0
count=0

while 0<=num<=100:
    if 60<=num<=100:
        total+=num
        count+=1
        print(total / count)
    num = int(input("enter number: "))

