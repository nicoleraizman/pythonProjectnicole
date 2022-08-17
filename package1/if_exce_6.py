grade=int(input("enter grade: "))


if 0<=grade<=100:
    if 70<=grade<=100:
        print("pass")
    elif 0<=grade<=70:
        print("fail")
else:
    print("invalid grade")