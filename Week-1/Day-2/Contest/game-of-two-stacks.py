def twoStacks(x, a, b):
    sum = 0
    count = 0
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        if sum > x:
            return count - 1
        elif sum == x:
            return count

        if i >= len(a):
            # pop out b and move j index
            sum += b[j]
            j += 1
            continue

        elif j >= len(b):
            # pop out a and move i index
            sum += a[i]
            i += 1
            continue

        if a[i] < b[j]:
            # pop out a and move i index
            sum += a[i]
            i += 1
            
        else:
            # pop out b and move j index
            sum += b[j]
            j += 1
        
        count += 1
        
    return count