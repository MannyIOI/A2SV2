# Complete the repeatedString function below.
def repeatedString(s, n):
    total = 0
    for i in range(n):
        if i >= len(s):
            break
        if s[i] == 'a': total += 1

    other = total * (n // len(s))
    for i in range(n % len(s)):
        if s[i] == 'a': other += 1

    return  other