# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        curr = root
        parent = [root]
        
        for i in preorder[1:]:
            node = TreeNode(i)
            if i < curr.val:
                curr.left = node
                curr = curr.left
            else:
                while len(parent) > 0 and parent[-1].val < i:
                    curr = parent.pop()
                
                if curr:
                    curr.right = node
                    curr = curr.right
            
            parent.append(node)
        
        return root