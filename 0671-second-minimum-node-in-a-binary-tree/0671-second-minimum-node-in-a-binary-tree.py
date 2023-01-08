# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.nodes = set()
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.nodes.add(node.val)
            dfs(node.right)
        
        dfs(root)
        
        minVal = root.val
        res = float('inf')
        
        for node in self.nodes:
            if minVal < node and node < res:
                res = node
        return int(res) if res < float('inf') else -1
        
            
        