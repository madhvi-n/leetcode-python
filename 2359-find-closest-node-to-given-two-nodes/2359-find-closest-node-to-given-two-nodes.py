class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node, dist, visit):
            visit[node] = True
            neighbor = edges[node]
            
            if neighbor != -1 and not visit[neighbor]:
                dist[neighbor] = 1 + dist[node]
                dfs(neighbor, dist, visit)
        
        n = len(edges)
        
        dist1, dist2 = [float('inf')] * n, [float('inf')] * n
        visit1, visit2 = [False] * n, [False] * n
        
        dist1[node1] = 0
        dist2[node2] = 0
        
        dfs(node1, dist1, visit1)
        dfs(node2, dist2, visit2)
        
        minDistNode = -1
        currMin = float('inf')
        
        for curr in range(n):
            if currMin > max(dist1[curr], dist2[curr]):
                minDistNode = curr
                currMin = max(dist1[curr], dist2[curr])
        
        return minDistNode