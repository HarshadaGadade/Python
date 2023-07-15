choice="y"
def evenorodd(n):
    if n % 2 == 0:
        print("Entered number is even", n)
    else:
        print("Entered number is odd", n)
def primenumber(num1):
    for i in range(2, num1):
        if num1 % i == 0:
            print("Not a prime Number")
            break
    else:
        print("is a prime number")
def calculator(num1,num2,ope):
        if ope == "add":
            ans=num1+num2
            print("Sumation of two numbers is:",ans)
        elif ope == "sub":
            ans=num1-num2
            print("Subtraction of two numbers is:",ans)
        elif ope == "mul":
            ans=num1*num2
            print("Multiplication of two numbers is:",ans)
        elif ope == "div":
            ans=num1/num2
            print("Division of two numbers is:",ans)
        elif ope == "isevenodd":
            evenorodd(num1)
        elif ope == "primenumber":
            primenumber(num1)
        else:
            print("Invalid choice")
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
while choice=="y" or choice=="Y":
    ch=input("Enter operation:")
    calculator(n1,n2,ch)
    choice=input("do u want to continue y/n:")
