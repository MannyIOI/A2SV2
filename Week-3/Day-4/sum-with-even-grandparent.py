# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        total = 0
        if root.val % 2 == 0:
            total += self.dfsSum(root)
            
        right = self.sumEvenGrandparent(root.right)
        left = self.sumEvenGrandparent(root.left)
        
        return total + right + left
    
    def dfsSum(self, root, level = 0):
        if root == None:
            return 0
        
        if level == 2:
            return root.val
        
        right = self.dfsSum(root.right, level + 1)
        left = self.dfsSum(root.left, level + 1)
        
        return right + left