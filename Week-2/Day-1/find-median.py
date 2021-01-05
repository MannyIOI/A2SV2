# Complete the findMedian function below.
def findMedian(arr):
    arr = sorted(arr)
    return arr[len(arr) // 2]   