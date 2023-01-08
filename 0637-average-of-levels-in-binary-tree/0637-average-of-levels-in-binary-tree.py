# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        res = []
        
        while queue:
            level = []
            nodes = []
            
            for node in queue:
                level.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            queue = nodes
            res.append(level)

        return [sum(level)/len(level) for level in res]
            
        
            