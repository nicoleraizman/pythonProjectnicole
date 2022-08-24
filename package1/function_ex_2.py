def valid_3digits(num):
    if 100<=num<=999:
        return True
    else:
        return False


num = int(input("enter number: "))
print(valid_3digits(num))

