def allCellsDistOrder(R, C, r0, c0):
    order = []
    diction = {}
    for i in range(R):
        for j in range(C):
            distance = manhattan_distance(r0, c0, i, j)
            if distance not in diction:
                diction[distance] = []
            diction[distance].append([i, j])
    
    for i in sorted(diction.keys()):
        order += diction[i]
    return order
    
def manhattan_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

print(allCellsDistOrder(2, 3, 1, 2))