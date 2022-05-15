# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        leaves = []
        queue = [root]
        level = []
        
        while queue:
            res = []
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)                
                if node.right is None and node.left is None:
                    res.append(node.val)
                
            if res:
                leaves.append(res)
            queue = level
            level = []
        return sum(leaves[-1])
        