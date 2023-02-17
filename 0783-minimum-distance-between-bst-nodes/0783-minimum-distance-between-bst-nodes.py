# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
        
#         def inorder(node):
#             if node:
#                 yield from inorder(node.left)
#                 yield node.val
#                 yield from inorder(node.right)
        
#         elements = list(inorder(root))
        
#         minDist = float('inf')
        
#         for i in range(1, len(elements)):
#             minDist = min(minDist, elements[i] - elements[i-1])
        
#         return minDist
        
        
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
        
                
        