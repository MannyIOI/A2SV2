class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        # binary search for the first target
        pos = [-1, -1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                pos[0] = mid
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        left = pos[0]
        right = len(nums) - 1
        # binary search for the next target
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                pos[1] = mid
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return pos