def sortColors(nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]: nums[i], nums[j] = nums[j], nums[i]
        
        return nums

nums = [2,0,2,1,1,0]
print(sortColors(nums))