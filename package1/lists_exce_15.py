num=int(input("how many fibonnaci numbers: "))

list1=[1,1]
for i in range(num):
    list1.append(list1[-1]+list1[-2])
print(list1)    