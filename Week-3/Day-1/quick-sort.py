def quickSort(arr):
    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] > pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])
    
    return left + [pivot] + right