# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def preorder(root):
            if root is None:
                return []
            
            elements = []
            if root is None:
                return
            
            if root.left: 
                elements += preorder(root.left)
            
            elements.append(root.val)
            
            if root.right:
                elements += preorder(root.right)
            return elements
        
        nodes = preorder(root)
        return len(nodes) if nodes else 0
        
