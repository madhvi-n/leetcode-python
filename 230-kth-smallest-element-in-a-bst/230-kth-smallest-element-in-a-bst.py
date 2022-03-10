# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list:
        elements = []
        
        if root is None:
            return None
        
        if root.left:
            elements += self.inorderTraversal(root.left)
        
        elements.append(root.val)
        
        if root.right:
            elements += self.inorderTraversal(root.right)
        
        return elements
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = self.inorderTraversal(root)
        return elements[k - 1]