choice = "y"
while choice == "y":
    mylist=[9,2,4]
    result=1
    for x in mylist:
        result=result*x
    print(result)
    choice = input("do u want to continue y/n:")