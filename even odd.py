choice ="y"
while choice=="y":
    n=int(input("Enter the number:"))
    print("Value for user entered number is",n)
    if n%2==0:
        print("Entered number is even",n)
    else:
        print("Entered number is odd",n)
    choice = input("do u want to continue y/n:")

