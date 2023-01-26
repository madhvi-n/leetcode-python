# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        
        queue = [root]
        res = []
        ans = []
        
        while queue:
            levels = []
            nodes = []
            for node in queue:
                if node:
                    nodes.append(node.val)
                if node.left:
                    levels.append(node.left)
                if node.right:
                    levels.append(node.right)
            queue = levels
            res.append(nodes)
        
        while res:
            ans.append(res.pop())
        
        return ans