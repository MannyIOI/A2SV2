import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        arr = []
        return sorted(c, key=c.get, reverse=True)[:k]