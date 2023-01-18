class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = defaultdict(list)
        visited = []
        
        for src, dest in paths:
            graph[src].append(dest)
        
        def dfs(node):
            if node in visited or node is None:
                return
            
            visited.append(node)
            
            for c in graph[node]:
                dfs(c)
            
        dfs(paths[0][0])
        return visited[-1]
    
        
        