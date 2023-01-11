class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        
        def calculate(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in seen or grid[row][col] == 0:
                return 0
            
            seen.add((row, col))
            
            subArea = calculate(row + 1, col) + calculate(row - 1, col) + \
                calculate(row, col + 1) + calculate(row, col - 1)
            return 1 + subArea
        
        
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                currentArea = calculate(r, c)
                maxArea = max(maxArea, currentArea)
        return maxArea