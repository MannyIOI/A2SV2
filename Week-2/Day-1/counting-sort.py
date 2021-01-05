def counting_sort(array):
    maximum = max(array)
    minimum = min(array)
    arr_len = 0
    if minimum < 0:
        arr_len = maximum + abs(minimum) + 1
    else:
        arr_len = maximum + 1

    count = [0] * (arr_len)

    zero_index = abs(minimum)

    for i in array:
        if i > 0:
            count[zero_index + i] += 1
        else:
            count[zero_index - abs(i)] += 1

    return count
    
array = [-2, 0, 1, 3, 6, 9, 9, 3, 5, 9]
print(counting_sort(array))