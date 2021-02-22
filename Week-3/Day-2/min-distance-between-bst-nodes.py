# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.inorder = []
        
        self.dfs(root)
        
        mini = 10 ** 5
        
        for i in range(len(self.inorder) - 1):
            mini = min(mini, self.inorder[i + 1] - self.inorder[i])
            
        return mini
    
    def dfs(self, root):
        if root == None:
            return
        
        self.dfs(root.left)
        self.inorder.append(root.val)
        self.dfs(root.right)