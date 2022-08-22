from random import randint

list1 = []
num=randint(1,50)
for i in range(10):
    list1.append(num)
    num=randint(1,50)
print(list1)
