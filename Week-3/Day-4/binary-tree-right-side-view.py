# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode, output=[]) -> List[int]:
        if root == None:
            return output
        
        output.append(root.val)
        
        if root.right:
            right_side = self.rightSideView(root.right)
        else:
            right_side = self.rightSideView(root.left)
        
        return right_side