class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        t = [0] + [float("inf")] * n
        graph = defaultdict(list)
        q = deque([(0, k)])
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        while q:
            time, node = q.popleft()
            if time < t[node]:
                t[node] = time
                for v, w in graph[node]:
                    q.append((time + w, v))
        
        max_time = max(t)
        return max_time if max_time < float("inf") else -1
        
        
        