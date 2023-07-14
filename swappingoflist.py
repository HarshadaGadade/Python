choice = "y"
while choice == "y":
    mylist=[12,35,9,56,24]
    get=(mylist[-1],mylist[0])
    mylist[0],mylist[-1]=get
    print("list after swapping",mylist)
    choice = input("do u want to continue y/n:")