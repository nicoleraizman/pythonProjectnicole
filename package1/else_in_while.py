grade=int(input("enter grade: "))
count=0

while 0<=grade<=100:
    count+=1
    if count==5:
        print("end!")
        break
    print("correct grade")
    grade = int(input("enter grade: "))

else:
    if grade<0 or grade>100:
        print("invalid grade")

