# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root == None:
            return None
        
        if val == root.val:
            return root
        
        right_search = self.searchBST(root.right, val)
        left_search = self.searchBST(root.left, val)
        
        if right_search != None and right_search.val == val:
            return right_search
        elif left_search != None and left_search.val == val:
            return left_search