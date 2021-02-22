import heapq
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        
        sort = sorted(c.items(), key=cmp_to_key(self.compare))
        ans = []
        
        for key, freq in sort:
            temp = [key] * freq
            ans += temp
        
        return ans
        
    def compare(self, x, y):
        if x[1] > y[1]:
            return True
        elif x[1] == y[1]:
            return y[0]-x[0]
        return -1