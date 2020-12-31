class Solution:
    def reverse(self, x: int) -> int:
        if x < 10 and x > -10: return x
        
        val = (abs(x) % 10) * 10 ** int(math.log10(abs(x)))
        val = val + self.reverse(abs(x) // 10)
        
        if val >= ((2 ** 31) - 1) or -val <= - 2 ** 31: return 0
        if x < 0: return -val
        return val
    
