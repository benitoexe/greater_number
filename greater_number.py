#function code
def find_max(a,b):
    if a > b:
        return a
    else:
        return b


#no fuction code
number1 = input("enter a number:  ")
number2 = input("enter another number:   ")
if number1 > number2:
    print(f"{number1} is greater")
else:
    print(f"{number2} is greater")
