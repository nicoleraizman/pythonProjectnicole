num1=int(input("enter num1: "))
# num2=int(input("enter num2: "))
# num3=int(input("enter num3: "))


if 100<=num1<=999:
    print("valid")
    if 100<=num1<=999:
        print(num1 % 10 + num1 // 10 % 10 + num1 // 100)

else:
    print("error")

# if 100<=num1<=999:
#     print(num1%10+num1//10%10+num1//100)
# else:
#     print("no")

# print(num1+num2+num3)