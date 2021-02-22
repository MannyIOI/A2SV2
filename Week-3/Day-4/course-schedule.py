# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode, count = 0) -> int:
        from collections import deque
        if not root:
            return 0
        
        queue = deque()
        queue.append((root, 1))
        while len(queue) > 0:
            q_item = queue.popleft()
            item = q_item[0]
            level = q_item[1]
            
            if item.left:
                queue.append((item.left, level + 1))
            
            if item.right:
                queue.append((item.right, level + 1))
            
            count = level
            
            if not item.left and not item.right:
                return count
        