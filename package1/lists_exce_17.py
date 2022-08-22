from random import randint

list1=[]
list2=[]

for i in range(5):
    num=int(randint(1,50))
    list1.append(num)
print(list1)

for item in range(5):
    num1=int(randint(1,50))
    list2.append(num1)
print(list2)

for i in list1:
    if i in list2:
        print("one common member")


