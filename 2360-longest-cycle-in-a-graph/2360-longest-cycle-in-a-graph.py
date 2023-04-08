class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans = -1
        n = len(edges)
        visited = [False] * n

        def dfs(node, edges, dist):
            nonlocal ans
            visited[node] = True
            neighbor = edges[node]

            if neighbor != -1 and not visited[neighbor]:
                dist[neighbor] = dist[node]+1
                dfs(neighbor,edges, dist)
                
            elif neighbor != -1 and neighbor in dist:
                ans = max(ans, dist[node]- dist[neighbor] + 1)

        for i in range(n):
            if not visited[i]:
                dist =  dict()
                dist[i] =1
                dfs(i, edges, dist)
        return ans