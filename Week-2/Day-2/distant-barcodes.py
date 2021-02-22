class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = collections.Counter(barcodes)
        
        ans = [None] * len(barcodes)
        idx = 0
        for i in sorted(c, key=c.get, reverse=True):
            for j in range(c[i]):
                if idx >= len(ans):
                    idx = 1
                if ans[idx] == None:
                    ans[idx] = i
                    idx += 2
        
        return ans
        
        