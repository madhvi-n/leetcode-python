# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        e1, e2 = [], []
        
        def dfs(node, elements):
            if node.right is None and node.left is None:
                elements.append(node.val)
            
            if node.left:
                dfs(node.left, elements)
            
            if node.right:
                dfs(node.right, elements)
        
        dfs(root1, e1)
        dfs(root2, e2)
        
        return e1 == e2