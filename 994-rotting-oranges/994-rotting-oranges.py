class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        levels = 0

        while queue:
            levels += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    r, c = x + dx, y + dy
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] = 2
                        queue.append((r, c))

        return -1 if fresh != 0 else max(levels - 1, 0)