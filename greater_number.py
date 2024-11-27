#function code
def find_max(a,b):
    if a > b:
        return a
    else:
        return b
print(find_max(11, 4))


#no fuction code
number1 = input("enter a number:  ")
number2 = input("enter another number:   ")
if number1 > number2:
    print(f"{number1} is greater")
if number2 > number1:
    print(f"{number2} is greater")
else:
    print(f"{number1} and {number2} are equal")
