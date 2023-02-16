# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(set)
        
        # O(n)
        stack = [(root, None)]
        while stack: 
            node, parent = stack.pop()
            if parent: 
                graph[parent.val].add(node.val)
                graph[node.val].add(parent.val)
            if node.left: 
                stack.append((node.left, node))
            if node.right: 
                stack.append((node.right, node))
        
        ans = -1
        seen = set([start])
        queue = deque([start])
        
        # O(n)
        while queue: 
            for _ in range(len(queue)): 
                u = queue.popleft()
                for v in graph[u]: 
                    if v not in seen: 
                        seen.add(v)
                        queue.append(v)
            ans += 1
        return ans 
        
