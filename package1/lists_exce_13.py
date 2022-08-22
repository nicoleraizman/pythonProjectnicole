from random import randint

list1=[]

for i in range(20):
    num=randint(1,100)
    list1.append(num)
print(list1)

num1 = int(input("enter number:"))
for i in list1:
    if i==num1:
        list1.remove(num1)
print(list1)













