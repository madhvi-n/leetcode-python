# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        def dfs(p, q, depth):
            if not p or not q:
                return
            
            if depth % 2 != 0:
                p.val, q.val = q.val, p.val
                
            dfs(p.left, q.right, depth + 1)
            dfs(p.right, q.left, depth + 1)
            
        
        dfs(root.left, root.right, 1)
        return root