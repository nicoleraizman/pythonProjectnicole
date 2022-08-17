num=""
total=0
count=0

for i in range(6):
    num=int(input("enter number: "))

    if num%2==0:
        total += num
        count += 1
print(total)
print(total/count)






