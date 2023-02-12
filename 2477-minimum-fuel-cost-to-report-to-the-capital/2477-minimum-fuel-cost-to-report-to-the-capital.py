class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        adj = [[] for _ in range(n)]
        degree = [0] * n

        for src, dest in roads:
            adj[src].append(dest)
            adj[dest].append(src)
            degree[src] += 1
            degree[dest] += 1

        return self.bfs(n, adj, degree, seats)

    def bfs(self, n, adj, degree, seats):
        queue = deque()
        for i in range(1, n):
            if degree[i] == 1:
                queue.append(i)

        representatives = [1] * n
        fuel = 0

        while queue:
            node = queue.popleft()
            fuel += ceil(representatives[node] / seats)
            for neighbor in adj[node]:
                degree[neighbor] -= 1
                representatives[neighbor] += representatives[node]
                if degree[neighbor] == 1 and neighbor != 0:
                    queue.append(neighbor)
        return fuel
        
        