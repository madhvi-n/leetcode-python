# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        elements = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            elements.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        min_val = 999
        for a, b in zip(elements, elements[1:]):
            min_val = min(min_val, b - a)        
        return min_val
