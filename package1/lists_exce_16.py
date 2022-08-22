
list1=[]
list2=[]
for i in range(7):
    num = int(input("enter numbers: "))
    list1.append(num)
print(list1)

for item in list1:
    if item not in list2:
        list2.append(item)
print(list2)














# list1=[1,1,2,5,4,7,7,9,3,5,1]
#
# if list1.count(1)>1 and list1.count(7)>1 and list1.count(5)>1:
#     list1.remove(1)
#     list1.remove(5)
#     list1.remove(7)
# print(list1)





