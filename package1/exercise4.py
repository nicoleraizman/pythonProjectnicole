name=input("enter name: ")
currentyear=int(input("enter current year: "))
age=int(input("enter age: "))
futureyear=int(input("enter future year: "))

hefresh=(futureyear-currentyear)
newage=(hefresh+age)

print(f"{name} will be {newage} in {futureyear}")


