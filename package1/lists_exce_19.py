from random import randint

list1=[]
list2=[]
list3=[]
for i in range(10):
    num=int(randint(1,9))
    list1.append(num)
print(list1)


for item in list1:
    if item not in list2:
        list2.append(item)
print(list2)

for it in list2:
    list3.append(list1.count(it))
print(list3)

for place in range(len(list2)):
    print(f'the digit {list2[place]}shows up {list3[place]}')


