class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
            
        for r in range(rows):
            for c in range(cols):
                perimeter += 4 * grid[r][c]
                
                if r > 0:
                    perimeter -= grid[r][c] * grid[r-1][c]
                
                if r < rows-1: 
                    perimeter -= grid[r][c] * grid[r+1][c]
                
                if c > 0:
                    perimeter -= grid[r][c] * grid[r][c-1]
                
                if c < cols-1:
                    perimeter -= grid[r][c] * grid[r][c+1]
                
        return perimeter