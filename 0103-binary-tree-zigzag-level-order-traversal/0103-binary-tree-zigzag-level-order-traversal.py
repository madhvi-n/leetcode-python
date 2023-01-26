# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        
        queue = [root]
        flag = False
        res = []
        
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
            if flag:
                res.append(nodes[::-1])
            else:
                res.append(nodes)
            
            flag = not flag
        
        return res