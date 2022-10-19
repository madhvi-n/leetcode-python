# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
#         def dfs(root):
#             if not root: 
#                 return [-1, -1, -1]
            
#             left, right = dfs(root.left), dfs(root.right)
#             return [left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])]
#         return dfs(root)[-1]

        self.max_ = 0
        
        def zigzag(node, is_left, count):
            
            if not node:
                return
            
            self.max_ = max(self.max_, count)
            
            if is_left:
                zigzag(node.right, False, count+1)
                zigzag(node.left, True, 1)
            else:
                zigzag(node.left, True, count+1)
                zigzag(node.right, False, 1)

            
        zigzag(root.left, True, 1)
        zigzag(root.right, False, 1)

        return self.max_
    
        