user_input = input("Enter the string")

reverse_string = user_input[::-1]
if(user_input == reverse_string):
    print("Given string is a palidrome")
else:
    print("Given string is not a Palidromre")