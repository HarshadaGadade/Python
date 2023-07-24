list = [3,2,3,4,3,15,3]
Search = 3

def searchOccurance(List,number):
    count = 0
    for i in list:
        if(i == number):
            count+=1
    return count

result = searchOccurance(list,Search)
if(result > 0):
    print('Count is:',result)
else:
    print('Element not found in the list.')