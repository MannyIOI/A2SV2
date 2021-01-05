# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices = sorted(prices)
    count = 0
    sum = 0
    for i in prices:
        if sum + i > k:
            return count
        sum += i
        count += 1