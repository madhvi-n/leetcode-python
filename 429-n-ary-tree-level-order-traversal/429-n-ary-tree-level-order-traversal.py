"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            qlength = len(q)
            level = []
            for i in range(qlength):
                node  = q.popleft()
                if node:
                    level.append(node.val)
                    for children in node.children:
                        q.append(children)
            if level:
                res.append(level)
        return res