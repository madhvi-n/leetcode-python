# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        
        result = []
        
        while queue:
            nodes, level = [], []
            for node in queue:
                if node:
                    nodes.append(node.val)
                    if node.left:
                        level.append(node.left)
                    
                    if node.right:
                        level.append(node.right)
            if nodes:
                result.append(nodes)
            queue = level
            level = []
        return result