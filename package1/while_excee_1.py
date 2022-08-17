num = int(input("enter three digit number: "))

while 100<=num<=999:
    print(num%10+num//100+num//10%10)
    num = int(input("enter three digit number: "))
if num>999 or num<100:
    print("invalid")