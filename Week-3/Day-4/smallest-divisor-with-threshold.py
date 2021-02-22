class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        mn_div = 1
        mx_div = max(nums)

        # binary search between mn_div and mx_div
        while mn_div <= mx_div:
            md_div = (mn_div + mx_div) >> 1
            md_sm = self.divided_sum(nums, md_div)
            
            if md_sm <= threshold:
                mx_div = md_div - 1
            else:
                mn_div = md_div + 1

        return mn_div
        
    def divided_sum(self, nums, divider):
        return sum([math.ceil(num / divider) for num in nums])