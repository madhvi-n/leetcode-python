# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        elements = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            elements.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return min(b - a for a, b in zip(elements, elements[1:]))