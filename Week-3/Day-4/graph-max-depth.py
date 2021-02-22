"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node', count = 0) -> int:
        if root == None:
            return count
        print(root.val)
        mx = count + 1
        for i in root.children:
            mx = max(self.maxDepth(i, count + 1), mx)
        
        return mx