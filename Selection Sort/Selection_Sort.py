def Selection_Sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallestIndex = 0
        smallestElement = arr[0]
        for i in range(1, len(arr)):
            if(arr[i] < smallestElement):
                smallestElement = arr[i]
                smallestIndex = i
        newArr.append(arr.pop(smallestIndex))
    return newArr


print(Selection_Sort([4, 3, 1, 5]))  # [1, 3, 4, 5]
