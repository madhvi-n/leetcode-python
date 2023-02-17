# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal prev, minDist
            if not node:
                return
            
            dfs(node.left)
            
            if prev:
                minDist = min(minDist, node.val - prev.val)
            
            prev = node
            
            dfs(node.right)
            
        prev = None
        minDist = float('inf')
        dfs(root)
        return minDist