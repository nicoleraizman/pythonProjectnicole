list1=[0,1,1,2,3,5]

print(list1)
print(list1[1])

list1[0]+=list1[4]
print(list1)

list1.append(120)
print(list1)

list1+=[2,9]
print(list1)

list1*=2
print(list1)

print(list1.index(120))
list1.append("hi")
print(list1)

print(list1.index("hi"))

print(list1.index(3 , 4))

print(list1.count(3))
print(list1.count('hi'))

list1.remove(1)
print(list1)

print(list1.remove(3))

list1.remove("hi")
print(list1)


