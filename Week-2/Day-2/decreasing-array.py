class Solution(object):
    def checkPossibility(self, nums):
        if len(nums) <= 1:
            return True
        count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1
                if count == 2:
                    return False
                if i - 2 >= 0 and nums[i - 2] > nums[i]: # have to promote nums[i]
                    nums[i] = nums[i - 1]
        return True