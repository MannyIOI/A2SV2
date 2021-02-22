# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left: TreeNode, right: TreeNode) -> bool:
        if (left == None and right != None) or (right == None and left != None):
            return False
        if left == None and right == None:
            return True
        
        if left.val != right.val:
            return False
        
        outer = self.helper(left.left, right.right)
        inner = self.helper(left.right, right.left)
        
        return (outer and inner)