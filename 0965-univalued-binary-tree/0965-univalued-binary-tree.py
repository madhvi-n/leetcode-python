# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, parent):
            if not node:
                return True
            
            if node.val != parent.val:
                return False
            
            return node.val == parent.val and dfs(node.left, node) and dfs(node.right, node)
        
        return dfs(root, root)