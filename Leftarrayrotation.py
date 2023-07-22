array = [1,2,3,4,5]
shift = 2

def printArray(array):
    for i in range(0,len(array)):
        print(array[i],end='')

def LeftRotation(array,shift):
    for i in range(0,shift):
        temp = array[0]
        for j in range(0,len(array) - 1):
            array[j] = array[j + 1]

        array[len(array) - 1] = temp
    return array

print("Array before Rotation:")
printArray(array)