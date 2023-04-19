# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest_path_length = 0

        def find_longest_zigzags(root):
            if root.left:
                _, child_longest_right = find_longest_zigzags(root.left)
                longest_left = child_longest_right + 1
            else:
                longest_left = 0

            if root.right:
                child_longest_left, _ = find_longest_zigzags(root.right)
                longest_right = child_longest_left + 1
            else:
                longest_right = 0
            
            self.longest_path_length = max(self.longest_path_length, longest_left, longest_right)
            return longest_left, longest_right
        
        find_longest_zigzags(root)
        return self.longest_path_length