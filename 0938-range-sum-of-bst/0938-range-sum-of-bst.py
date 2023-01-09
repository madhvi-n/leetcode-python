# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         rangeSum = 0
        
#         def inorder(node):
#             if node:
#                 yield from inorder(node.left)
#                 yield node.val
#                 yield from inorder(node.right)
        
#         for val in inorder(root):
#             if val >= low and val <= high:
#                 rangeSum += val
        
#         return rangeSum

        self.rangeSum = 0
    
        def dfs(node):
            if not node:
                return 0
            
            if node.val >= low and node.val <= high:
                self.rangeSum += node.val
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.rangeSum