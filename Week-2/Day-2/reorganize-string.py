class Solution:
    def reorganizeString(self, S: str) -> str:
        c = collections.Counter(S)
    
        arr = [None] * len(S)

        idx = 0
        for i in sorted(c, key=c.get, reverse=True):
            for j in range(c[i]):
                if idx >= len(arr):
                    idx = 1
                if arr[idx] == None:
                    arr[idx] = i
                    if idx > 0 and arr[idx - 1] == arr[idx]:
                        return ''
                    if idx < len(S) - 1 and arr[idx + 1] == arr[idx]:
                        return '' 
                    idx += 2

        return ''.join(arr)
