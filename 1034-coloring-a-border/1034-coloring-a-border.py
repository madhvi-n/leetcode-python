class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        
        
        def helper(x, y, c):
            if (x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != c): 
                return
            grid[x][y] = -c
            
            helper(x - 1, y, c)
            helper(x + 1, y, c)
            helper(x, y - 1, c)
            helper(x, y + 1, c)
            
            if (x > 0 and x < rows - 1 and y > 0 and y < cols - 1 and\
                    c == abs(grid[x - 1][y]) and c == abs(grid[x + 1][y]) and\
                        c == abs(grid[x][y - 1]) and c == abs(grid[x][y + 1])):
                grid[x][y] = c
                
                
        helper(row, col, grid[row][col])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    grid[r][c] = color
        
        return grid