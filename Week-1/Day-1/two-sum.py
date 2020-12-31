class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(nums)):
            if target - nums[i] in prevMap and prevMap[target - nums[i]] != i: 
                return [prevMap[target - nums[i]], i]
            if not nums[i] in prevMap: prevMap[nums[i]] = i
