# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int, currSum = 0) -> bool:
        if root == None:
            return False
        
        currSum = currSum + root.val
        
        if currSum == targetSum and not root.left and not root.right:
            return True
        
        left_exists = self.hasPathSum(root.left, targetSum, currSum)
        right_exists = self.hasPathSum(root.right, targetSum, currSum)
        
        return left_exists or right_exists
        