class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [False] * n
        components = 0
        edges = len(connections)
        
        # create adjacency list for graph
        for src, dest in connections:
            graph[src].append(dest)
            graph[dest].append(src)
        
        # dfs function
        def dfs(src, visited):
            visited[src] = True
            
            for adjacent in graph[src]:
                if not visited[adjacent]:
                    dfs(adjacent, visited)
        
        # find no of components using dfs
        for i in range(n):
            if not visited[i]:
                dfs(i, visited)
                components += 1
        
        # if edges are less than of required edges for a connected graph, return -1
        if edges < n - 1:
            return -1
        
        # calculate redundant edges using formula
        redundant_edges = edges - ((n - 1) - (components - 1))
        if redundant_edges >= components - 1:
            return components - 1
        return -1
                