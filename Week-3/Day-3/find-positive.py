"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        y = 1000
        x = 1
        ans = []
        while y > 0 and x <= 1000:
            val = customfunction.f(x, y)
            if val < z:
                x += 1
            elif val > z:
                y = y - 1
            else:
                ans.append([x, y])
                x = x + 1
        
        return ans