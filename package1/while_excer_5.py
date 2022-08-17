num = int(input("enter a two digit number: "))

while 10<=num<=99:
    if num%7==0 or num//10==7 or num%10==7:
        print("lucky number")
        num = int(input("enter a two digit number: "))
