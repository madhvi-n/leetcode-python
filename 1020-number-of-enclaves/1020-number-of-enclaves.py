class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def dfs(row, col):
            if row < 0 or col < 0 or row == ROWS or col == COLS or not grid[row][col] or (row, col) in visited:
                return 0
            visited.add((row, col))
            res = 1
            for dx, dy in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                res += dfs(dx, dy)
            return res
        
        land, borderLand = 0, 0
        
        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c]
                
                if grid[r][c] == 1 and (r, c) not in visited and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    borderLand += dfs(r, c)
        
        return land - borderLand