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
            nodes = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if nodes:
                res.append(nodes)
        
        while res:
            ans.append(res.pop())
        
        return ans