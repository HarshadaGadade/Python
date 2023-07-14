choice = "y"
while choice == "y":
    import math
    n=int(input("enter the number:"))
    result=math.factorial(n)
    print("Factorial of",n,"is",result)
    choice = input("do u want to continue y/n:")