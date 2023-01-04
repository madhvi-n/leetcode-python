# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        result = dict()
        curr_height = 1

        while queue:
            level = []
            curr_sum = 0
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                curr_sum += node.val
            queue = level
            result[curr_height] = curr_sum
            curr_height += 1
        
        total, level = float('-inf'), 0
        for key, val in result.items():
            if val > total:
                total, level = val, key
        return level