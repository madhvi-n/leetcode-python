class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
            rotten = set()
            rows, cols = len(grid), len(grid[0])
            fresh = 0

            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 2:
                        rotten.add((i, j))
                    if grid[i][j] == 1:
                        fresh += 1
            levels = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            while rotten:
                levels += 1
                temp = set()
                for (x, y) in rotten:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh -= 1
                            temp.add((nx, ny))
                rotten = temp
            return max(levels - 1, 0) if fresh == 0 else -1