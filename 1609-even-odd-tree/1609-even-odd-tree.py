# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        is_even = True
        
        while queue:
            level = []
            prev = None
            for node in queue:
                if is_even:
                    if node.val % 2 == 0: 
                        return False
                    if prev and prev.val >= node.val: 
                        return False
                else:
                    if node.val % 2 == 1: 
                        return False
                    if prev and prev.val <= node.val: 
                        return False
                
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                prev = node
            queue = level
            is_even = not is_even
        return True