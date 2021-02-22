# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # choose max
        # construct maximum binary trees on left and right
        # attach them to max
        
        if len(nums) == 0:
            return
        
        max_idx = nums.index(max(nums))
        
        left_tree = self.constructMaximumBinaryTree(nums[:max_idx])
        right_tree = self.constructMaximumBinaryTree(nums[max_idx + 1:])
        
        root = TreeNode(val=nums[max_idx])
        root.left = left_tree
        root.right = right_tree
        
        return root