def sortColors(nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        left = 0
        right = len(nums) - 1
        while i < right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
        
        return nums



nums = [2,0,2,1,1,0]
print(sortColors(nums))