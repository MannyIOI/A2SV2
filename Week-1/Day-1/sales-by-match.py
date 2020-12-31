# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    matched = {}
    for i in ar:
        if not i in matched.keys(): matched[i] = 1
        else: matched[i] += 1
    count = 0
    for i in matched.values():
        count += i // 2
    
    return count
