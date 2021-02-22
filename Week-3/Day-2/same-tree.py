# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # check val of both nodes if not equal return false
        # check right side of tree
        # check left side of tree
        if p == None and q == None:
            return True
        if (p == None and q != None) or (q == None and p != None):
            return False
        
        if p.val != q.val:
            return False
        
        # if self.isLeaf(p) and self.isLeaf(q):
        #     if p.val == q.val:
        #         return True
        #     else:
        #         return False
        
        left_check = self.isSameTree(p.left, q.left)
        right_check = self.isSameTree(p.right, q.right)
        
        return (left_check and right_check)
    
    def isLeaf(self, node: TreeNode):
        if node.left == None and node.right == None:
            return False
        return True