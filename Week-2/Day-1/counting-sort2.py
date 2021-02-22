def countingSort(arr):
    count = [0] * (max(arr) + 1)
    sorted = []
    for i in arr:
        count[i] += 1

    
    for i in range(len(count)):
        sorted += [i] * count[i]
    
    return sorted
    