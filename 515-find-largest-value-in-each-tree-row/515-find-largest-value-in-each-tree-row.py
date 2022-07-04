# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        nodes = defaultdict(list)
        result = []
        
        def dfs(node, depth):
            nonlocal nodes
            if node is None:
                return
            
            nodes[depth].append(node.val)
            
            if node.left:
                dfs(node.left, depth + 1)
            
            if node.right:
                dfs(node.right, depth + 1)
        
        dfs(root, 0)
        
        for depth, values in nodes.items():
            result.append(max(values))
        
        return result