# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
    
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_sum, right_sum = dfs(node.left), dfs(node.right)
            max_single_pathsum = max(node.val + max(left_sum, right_sum), node.val)
            max_sum = max(max_sum, max_single_pathsum, node.val + left_sum + right_sum)
            return max_single_pathsum
        
        dfs(root)
        return max_sum