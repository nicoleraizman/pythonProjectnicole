# from random import randint
#
# list1=[ ]
# for i in range(10):
#     list1.append(randint(1,100))
# print(list1)

list1=[15,55,65,98,87,33,6]
for i in range(len(list1)):
    list1[i]*=2
print(list1)

print(list1[1:5])
print(list1[ : :-1])

print(list1[4:1:-1])
list2=list1[-3:]+list1[:3]+[10,20,30,40]
print(list2)

