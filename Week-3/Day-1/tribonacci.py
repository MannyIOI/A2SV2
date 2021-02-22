class Solution:
    def tribonacci(self, n: int) -> int:
        trib_0 = 0
        trib_1 = 1
        trib_2 = 1
        
        if n == 0:
            return trib_0
        elif n == 1:
            return trib_1
        elif n == 2:
            return trib_2
        
        for i in range(n - 2):
            temp = trib_2
            trib_2 = trib_0 + trib_1 + trib_2
            trib_0 = trib_1
            trib_1 = temp
        
        return trib_2