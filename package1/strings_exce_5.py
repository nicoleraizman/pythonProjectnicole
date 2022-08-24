word=str(input("enter a word: "))
letter = str(input("enter a letter: "))
count=0

for i in range(len(word)):
    if word[i]==letter:
        count+=1
print(count)








# if letter in word:
#     count+=1
#     print(count)
# else:
#     print("no")

