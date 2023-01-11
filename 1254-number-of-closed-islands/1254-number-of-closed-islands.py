class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def mark_closed_island(row, col):
            # if row, col is out of bounds, return false and if current cell is 1, return True
            # change the current cell to 1 and check for closed islands in all 4 directions recursively
            # return top and bottom and left and right
            
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return False
            
            if grid[row][col] == 1:
                return True
            
            grid[row][col] = 1
            visited.add((row, col))
            
            top = mark_closed_island(row - 1, col)
            bottom = mark_closed_island(row + 1, col)
            left = mark_closed_island(row, col - 1)
            right = mark_closed_island(row, col + 1)
            return top and bottom and left and right
        
        # for each cell starting from 1st row to n - 1 rows and cols
        # if current grid cell is 0 and not visited, check for closed islands
        # if true, increment closed island count by 1
        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0 and (r, c) not in visited:
                    if mark_closed_island(r, c):
                        closed_islands += 1
        
        return closed_islands