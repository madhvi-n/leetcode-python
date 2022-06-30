class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjacency_list = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjacency_list[i].append([dist, j])
                adjacency_list[j].append([dist, i])

        result = 0
        visited = set()
        min_heap = [[0, 0]]  # [cost, point]
        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            result += cost
            visited.add(i)

            for adjacent_cost, adjacent in adjacency_list[i]:
                if adjacent not in visited:
                    heapq.heappush(min_heap, [adjacent_cost, adjacent])
        return result