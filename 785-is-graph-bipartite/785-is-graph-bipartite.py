class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adjacency_list = defaultdict(list)
        n = len(graph)
        
        for index in range(n):
            if graph[index]:
                adjacency_list[index].extend(graph[index])
        
        visited = [False] * n
        color = [False] * n
        
        src = 0
        visited[src] = True
        
        def dfs(v):
            for u in graph[v]:
                if not visited[u]:
                    visited[u] = True
                    color[u] = not color[v]
                    
                    if not dfs(u):
                        return False
                    
                elif color[v] == color[u]:
                    return False
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
        return True