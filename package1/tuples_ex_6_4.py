from random import randint

list1=[]
for i in range(10):
    num=randint(1,100)
    list1.append(num)
print(list1)


print(tuple(list1))


# num1=int(input("enter a number: "))
# list1+=(num1,)
# print(list1)
t1=(list1[0:4]+list1[-4:])

print(t1)

print(t1[1:])

