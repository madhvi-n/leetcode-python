# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node) -> bool:
            if node is None:
                return False
            
            left = dfs(node.left)
            
            right = dfs(node.right)
            
            if not left:
                node.left = None
            
            if not right:
                node.right = None
            
            return node.val or left or right
        return root if dfs(root) else None