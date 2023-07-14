choice = "y"
while choice == "y":
    mylist=[5,10,15,20]
    total=0
    for i in range(0,len(mylist)):
        total=total+mylist[i]
    print("sum of all elements in given list:",total)
    choice = input("do u want to continue y/n:")



