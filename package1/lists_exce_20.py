from random import randint

list1=[]
for i in range(5):
    num=int(randint(1,10))
    list1.append(num)
print(list1)

# num=int(input("enter number"))

for item in list1:
    num1 = int(input("enter number"))
    if num1 in list1:
        place=list1.index(num1)
        print(place)
    else:
        print("doesnt exist!!!")



