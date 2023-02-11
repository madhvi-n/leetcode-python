class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        R, B = 0, 1
        
        graph = defaultdict(list)
        
        for v, w in redEdges:
            graph[v].append((w, R))
        
        for v, w in blueEdges:
            graph[v].append((w, B))
            
        queue = deque([(0, 0, -1)])
        visited = set()
        res = [-1] * n
        dist = defaultdict(int)
        
        while queue:
            d, v, vcolor = queue.popleft()
            if (v, vcolor) in visited: 
                continue
            visited.add((v, vcolor))
            
            if v not in dist: 
                dist[v] = d
            res[v] = dist[v]
            
            for w, color in graph[v]:
                if vcolor != color:
                    queue.append((d+1, w, color))
        return res