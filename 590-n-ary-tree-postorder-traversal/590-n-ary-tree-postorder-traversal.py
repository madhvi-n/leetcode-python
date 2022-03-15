"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        elements = []

        if root is None:
            return None

        if root.children:
            for children in root.children:
                elements += self.postorder(children)

        elements.append(root.val)

        return elements