
list1=[]
for i in range(5):
    word = str(input("enter a word: "))
    list1.append(word)
print(list1)

count=0
for item in list1:
    if len(item)>=4 and item[-1:]==item[0]:
        count+=1
print(count)







