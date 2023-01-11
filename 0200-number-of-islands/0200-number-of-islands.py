class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != "1":
                return
            
            grid[row][col] = "2"
            
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands
            
            