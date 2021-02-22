# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # find right sum if in range
        # find left sum if in range
        # evaluate self.sum if in range
        # add left and right
        
        if root == None:
            return 0
        
        
        if root.left == None and root.right == None:
            if root.val >= low and root.val <= high:
                return root.val
            return 0

        
        right_sum = self.rangeSumBST(root.right, low, high)
        left_sum = self.rangeSumBST(root.left, low, high)
        
        if root.val >= low and root.val <= high:
            return root.val + left_sum + right_sum
        
        return left_sum + right_sum