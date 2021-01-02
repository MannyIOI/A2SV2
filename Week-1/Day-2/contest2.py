import math

# def repeatedString(s, n):
#     total = 0
#     for i in range(n):
#         if i >= len(s):
#             break
#         if s[i] == 'a': total += 1

#     other = total * (n // len(s))
#     for i in range(n % len(s)):
#         if s[i] == 'a': other += 1

#     return  other

# s = 'bca'
# n = 10


# print(repeatedString(s, n))

# Complete the divisibleSumPairs function below.
# def divisibleSumPairs(n, k, ar):
#     total = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if (ar[i] + ar[j]) % k == 0:
#                 total += 1
    
#     return total

# print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))


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

x = 10
a = [4, 2, 4, 6, 1]
b = [5, 1, 8, 5]
print(twoStacks(x, a, b))