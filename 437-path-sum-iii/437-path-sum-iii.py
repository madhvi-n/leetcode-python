# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        self.dfs(root, targetSum)
        return self.paths
    
    def dfs(self, node, target):
        if node is None:
            return
        self.checkPathSum(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)
    
    def checkPathSum(self, node, target):
        if node is None:
            return
        
        if node.val == target:
            self.paths += 1
        
        self.checkPathSum(node.left, target - node.val)
        self.checkPathSum(node.right, target - node.val)
        