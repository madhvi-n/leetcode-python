class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        
        def dfs(node, dest, visited):
            if node == dest:
                return True
            
            if node in visited:
                return False
            
            visited.add(node)
            
            for child in graph[node]:
                if dfs(child, dest, visited):
                    return True
            return False
        return dfs(source, destination, visited)