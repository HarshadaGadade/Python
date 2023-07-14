choice = "y"
while choice == "y":
    mylist=[1,6,3,5,3,4]
    ele=9
    flag=0
    for i in mylist:
        if(i==ele):
            print("Element found")
            flag=1
            break
    if(flag==0):
        print("element not found")
    choice = input("do u want to continue y/n:")

