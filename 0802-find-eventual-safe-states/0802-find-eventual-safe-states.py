class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        safe = [False] * N
        
        # graph = [set(neighbors) for neighbors in graph]
        adjacency_list = defaultdict(set)
        queue = deque()
        
        for src, dest in enumerate(graph):
            if not dest:
                queue.append(src)
            
            for d in dest:
                adjacency_list[d].add(src)
        
        
        while queue:
            n = queue.popleft()
            
            safe[n] = True
            
            for i in adjacency_list[n]:
                graph[i].remove(n)
                
                if len(graph[i]) == 0:
                    queue.append(i)
        return [i for i, is_safe in enumerate(safe) if is_safe]
    
