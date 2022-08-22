# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if node is None:
                return 0
            
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)
            
            left = right = 0
            
            if node.left and node.left.val == node.val:
                left = leftPath + 1
            
            if node.right and node.right.val == node.val:
                right = rightPath + 1
            
            self.ans = max(self.ans, left + right)
            return max(left, right)
        dfs(root)
        return self.ans