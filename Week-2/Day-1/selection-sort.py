def selection_sort(array):
    for i in range(len(array)):
        curr_min_index = i
        for j in range(i, len(array)):
            if array[j] <= array[curr_min_index]:
                curr_min_index = j
        array[curr_min_index], array[i] = array[i], array[curr_min_index]

    return array

array = [-2, 0, 1, 3, 6, 9, 9, 3, 5, 9]
print(selection_sort(array))