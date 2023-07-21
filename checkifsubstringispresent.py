sentence = "My name is Roshan"
substring = "Roshan"

def searchstring(substring):
    result = sentence.find(substring)
    if(result == -1):
        print("Given substring not found")
    else:
        print("Substring found at index:",result)

searchstring(substring)
