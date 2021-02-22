class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_ = sorted(citations)
        # curr = sorted_[0]
        h = 0
        for i in range(len(sorted_) - 1, -1, -1):
            if h < sorted_[i]:
                h += 1
            elif h == sorted_[i]:
                return h
            elif h > sorted_[i]:
                break
        return h
    
# 6, 5, 3, 1, 0
# 0