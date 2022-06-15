class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        if graph is None:
            return []
        
        adjacency_list = defaultdict(list)
        
        for index in range(len(graph)):
            adjacency_list[index] += graph[index]
            
        
        visited = [False] * len(graph)
        path = []
        result = []
        
        def dfs(source, destination, visited, path):
            visited[source] = True
            path.append(source)
            
            if source == destination:
                result.append(path[:])
        
            else:
                for v in adjacency_list[source]:
                    if not visited[v]:
                        dfs(v, destination, visited, path)
        
            path.pop()
            visited[source] = False
        
        
        dfs(0, len(graph) - 1, visited, path)
        return result
        
            
        