def insertion_sort(array):
    for i in range(len(array)):
        for j in range(i + 1, -1, -1):
            print(i)
            if i + 1 >= len(array):
                continue

            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]
    
    return array

print(insertion_sort([3, 2]))

# for i in range(0, -1, -1):
#     print(i)