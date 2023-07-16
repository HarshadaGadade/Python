# choice ="y"
# while choice=="y":
#     def factorial(n):
#         return 1 if(n == 1 or n == 2) else n*factorial(n-1)
#     num=14
#     print("factorial of",num,"is",factorial(num))
#     choice = input("do u want to continue y/n:")
n = int(input("Enter the number:"))
factorial = 1
for i in range (1 , n+1):
        factorial = factorial * i
print("Factorial of ",n," is :",factorial)