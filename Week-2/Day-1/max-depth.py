class Solution:
    def maxDepth(self, s: str) -> int:
        maxDp = 0
        count = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
            
            maxDp = max(count, maxDp)
        
        return maxDp