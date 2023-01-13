class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        queue = [(0, 0, 1)] # (row, col, distance)
        
        for row, col, dist in queue:
            if row == n - 1 and col == n - 1:
                return dist
            
            for x, y in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1),
                        (row + 1, col + 1), (row - 1, col -1), (row + 1, col - 1), (row - 1, col + 1)
                        ]:
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    queue.append((x, y, dist + 1))
        
        return -1