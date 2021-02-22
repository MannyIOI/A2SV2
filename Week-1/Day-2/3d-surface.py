def surfaceArea(A):
    total = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(i, j, total)
            if i == 0:
                total += A[i][j]
            if j == 0:
                total += A[i][j]
            if i == len(A) - 1:
                total += A[i][j]
            if j == len(A[0]) - 1:
                total += A[i][j]
            if j < len(A[0]) - 1:        
                total += abs(A[i][j] - A[i][j + 1])
            if i < len(A) - 1:
                total += abs(A[i][j] - A[i + 1][j])
    
    total += 2 * len(A) * len(A[0])
    
    return total