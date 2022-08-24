def sum_digits(num):
    return num%10+num//10%10+num//100

num=int(input("enter a 3 digit number: "))

print(sum_digits(num))
