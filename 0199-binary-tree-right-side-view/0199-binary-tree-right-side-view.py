# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return root
        
        self.result = []
        queue = [root]
        level_order = []

        while queue:
            next_level = []
            current_level = []
            for node in queue:
                if node:
                    current_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            self.result.append(node.val)
            queue = next_level
            level_order.append(current_level)
        
        return self.result