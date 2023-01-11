class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def calculate(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] in [0, 2]:
                return 0
            
            grid[row][col] = 2
            
            subArea = calculate(row + 1, col) + calculate(row - 1, col) + \
                calculate(row, col + 1) + calculate(row, col - 1)
            return 1 + subArea
        
        
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    currentArea = calculate(r, c)
                    maxArea = max(maxArea, currentArea)
        return maxArea