import numpy

def mergesort(inputArray):
    if len(inputArray) > 1:
        left = []
        right = []

        for x in range(len(inputArray)):
            if x < len(inputArray)//2:
                left.append(inputArray[x])
            else:
                right.append(inputArray[x])

        left = mergesort(left)
        right = mergesort(right)

        merged = []

        while(len(left) > 0 and len(right) > 0):
            if left[0] >= right[0]:
                merged.append(right[0])
                right.pop(0)
            else:
                merged.append(left[0])
                left.pop(0)

        while(len(left) > 0):
            merged.append(left[0])
            left.pop(0)

        while(len(right) > 0):
            merged.append(right[0])
            right.pop(0)

        return merged

    else:
        return inputArray


unsorted_array = [3,4,53,2,55,45,34,34,564,5,34,3,556,5646,4,54,6,56,3,75,6,45,3,4,564]
                                                 
print(mergesort(unsorted_array))
