class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        
        for src, dest in connections:
            graph[src].append(dest)
            graph[dest].append(src)
        
        time = 0
        disc = [-1] * n
        low = [-1] * n
        parent = [-1] * n
        visited = [False] * n
        bridges = []
        
        def dfs(src, visited, disc, low, parent, time):
            visited[src] = True
            disc[src] = low[src] = time
            time += 1
            
            for adjacent in graph[src]:
                if not visited[adjacent]:
                    parent[adjacent] = src
                    dfs(adjacent, visited, disc, low, parent, time)
                    low[src] = min(low[src], low[adjacent])


                    if low[adjacent] > disc[src]:
                        bridges.append([src, adjacent])
                
                elif adjacent != parent[src]:
                    low[src] = min(low[src], disc[adjacent])
        
        for i in range(n):
            if not visited[i]:
                dfs(i, visited, disc, low, parent, time)
        
        return bridges