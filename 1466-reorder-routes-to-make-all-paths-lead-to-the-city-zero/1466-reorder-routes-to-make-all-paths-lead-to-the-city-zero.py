class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        edges = {(a, b) for a, b in connections}
        
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        changes = 0
        
        def dfs(city):
            nonlocal visited, changes, edges
            
            for neighbor in graph[city]:
                if neighbor in visited:
                    continue
                
                if (neighbor, city) not in edges:
                    changes += 1
                visited.add(neighbor)
                dfs(neighbor)
        
        visited.add(0)
        dfs(0)
        return changes
                    