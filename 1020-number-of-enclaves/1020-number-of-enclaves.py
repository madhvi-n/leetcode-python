class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0 or (row, col) in visited:
                return
            
            visited.add((row, col))
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                dfs(new_row, new_col)
            
        
        for r in range(rows):
            # first column
            if grid[r][0] == 1 and (r, 0) not in visited:
                dfs(r, 0)
                
            # last column
            if grid[r][cols - 1] == 1 and (r, cols - 1) not in visited:
                dfs(r, cols - 1)
        
        for c in range(cols):
            # first row
            if grid[0][c] == 1 and (0, c) not in visited:
                dfs(0, c)
            
            # last row
            if grid[rows - 1][c] == 1 and (rows - 1, c) not in visited:
                dfs(rows - 1, c)
        
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    count += 1
        
        return count