# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.pair = [-1, 0]
        if root.left == None and root.right == None:
            return root.val
        self.dfs(root)
        return self.pair[1]
        
    def dfs(self, root: TreeNode, count=0):
        if root == None:
            return
        
        self.dfs(root.left, count + 1)
        
        if count > self.pair[0]:
            self.pair[0] = count
            self.pair[1] = root.val
            
        self.dfs(root.right, count + 1)