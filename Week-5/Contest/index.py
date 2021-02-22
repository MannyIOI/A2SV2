# # Complete the strangeCounter function below.
# def strangeCounter(t):
#     counter = 3
#     test = counter
    
#     while t - test > 0:
#         test = test + counter * 2
#         counter = counter * 2
#     return test - t + 1


# for i in range(22):
#     print(strangeCounter(i + 1))
# print(strangeCounter(21))
# print(strangeCounter(17))
# print(strangeCounter(13))
# print(strangeCounter(10))
# print(strangeCounter(5))
# print(strangeCounter(4))
# print(strangeCounter(6))

def cavityMap(grid):
    for i in range(len(grid)):
        if i == 0 or i == len(grid) - 1:
            continue
        for j in range(len(grid[i])):
            if j == 0 or j == len(grid[i]) - 1:
                continue
            
            if grid[i][j] > grid[i - 1][j] and \
                grid[i][j] > grid[i][j - 1] and \
                grid[i][j] > grid[i + 1][j] and \
                grid[i][j] > grid[i][j + 1]:
                    print(grid[i])
                    print(list(grid[i]))
                    tmp = list(grid[i])
                    tmp[j] = 'X'
                    print(''.join(tmp))
                    grid[i] = ''.join(tmp)
        
    return grid


cavityMap(['1112', '1912', '1892', '1234'])