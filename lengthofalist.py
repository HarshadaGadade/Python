choice = "y"
while choice == "y":
    mylist=[1,4,6,7,8,10,12,14,15]
    print(mylist)

    count=0
    for i in mylist:
        count=count+1
    print("Length of the list is:",count)
    mylist=[1,4,6,7,8,10,12,14,15]
    print(mylist)
    print("length of list using len() method is:",len(mylist))
    choice = input("do u want to continue y/n:")
