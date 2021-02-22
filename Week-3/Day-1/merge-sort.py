class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums

        mid = (len(nums) // 2) 
        # print(nums[:mid], nums[mid:])

        right_merged = self.sortArray(nums[:mid])
        left_merged = self.sortArray(nums[mid:])

        return merge(right_merged, left_merged)
    
    def merge(left, right):
        arr = []
        i = 0
        j = 0
        while i < len(left) or j < len(right):
            if j >= len(right):
                arr += left[i:]
                break
            if i >= len(left):
                arr += right[j:]
                break

            if left[i] > right[j]:
                arr.append(right[j])
                j += 1
            else:
                arr.append(left[i])
                i += 1
        return arr