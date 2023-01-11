class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        def mark_current_island(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != "1":
                return
            
            grid[row][col] = "2"
            
            mark_current_island(row + 1, col)
            mark_current_island(row - 1, col)
            mark_current_island(row, col + 1)
            mark_current_island(row, col - 1)
            
        islands = 0
        
        # Check for every possible island for each cell of grid using dfs recursively
        # for each island, increment the count, keep track of visited by adding it in visited set or marking it in place
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    mark_current_island(r, c)
                    islands += 1
        return islands
            
            