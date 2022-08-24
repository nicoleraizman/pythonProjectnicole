d1={1:10,2:20,3:30,4:30,5:20}
d2={}
list1=[]
for i in d1:
    if d1[i] not in list1:
        list1.append(d1[i])
        d2.update({i:d1[i]})
print(d2)







