# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        mapping = dict()
        
        for parent, child, left in descriptions:
            parent_node = mapping.setdefault(parent, TreeNode(parent))
            child_node = mapping.setdefault(child, TreeNode(child))
            
            if left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            children.add(child)
            
        root = (set(mapping) - set(children)).pop()
        return mapping[root]
            