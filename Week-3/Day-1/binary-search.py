class Solution:
    def search(self, nums: [int], target: int) -> int:
        low, high = 0, len(nums) - 1
        md = (high + low) // 2
        
        if nums[0] == target:
            return 0
        
        while low < high:
            if target > nums[md]:
                low = md + 1
            elif target < nums[md]:
                high = md
            else:
                return md
            
            md = (high + low) // 2
        
        if target == nums[md]:
            return len(nums) - 1
        
        return -1