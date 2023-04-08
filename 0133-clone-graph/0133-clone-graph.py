"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
#         visited = dict()
        
#         def clone(current_node):
#             if current_node is None:
#                 return
            
#             if current_node in visited:
#                 return visited[current_node]
            
#             copy = Node(current_node.val)
#             visited[current_node] = copy
            
#             for adjacent in current_node.neighbors:
#                 copy.neighbors.append(clone(adjacent))
#             return copy
        
#         return clone(node)
            
        if node is None:
            return

        visited = dict()
        queue = deque([node])
        visited[node] = Node(node.val)

        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[current_node].neighbors.append(visited[neighbor])
        return visited[node]