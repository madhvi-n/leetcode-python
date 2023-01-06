# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = "~"

        def dfs(node, array):
            if node:
                array.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.ans = min(self.ans, "".join(reversed(array)))

                dfs(node.left, array)
                dfs(node.right, array)
                array.pop()

        dfs(root, [])
        return self.ans