"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        elements = []
        
        if root is None:
            return None
        
        elements.append(root.val)
        
        if root.children:
            for children in root.children:
                elements += self.preorder(children)
        
        return elements
        
        
        