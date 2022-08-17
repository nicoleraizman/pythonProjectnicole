num=int(input("enter a two digit number: "))

if 10<=num<=99:
    if num%7==0 or num%10==7 or num//10%10==7:
        print("lucky number")
    else:
        print("")
else:
    print("error")
