# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if root is None, return False
        # if root is leaf, check root val against targetSum
        # Run dfs on left and right node, targetSum - root.val
        
        if root is None:
            return False
        
        if not root.left and not root.right and root.val == targetSum:
            return True
            
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)