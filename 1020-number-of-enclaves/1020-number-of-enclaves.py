class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(row, col):
            # if row or col is out of bounds or current cell in grid is 0 or visited, return
            if row < 0 or row >= rows or col < 0 or col >= cols or\
                grid[row][col] == 0 or visited[row][col]:
                return
            
            # mark current cell as visited and traverse in 4 directions
            visited[row][col] = True
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        
        for r in range(rows):
            # first column
            if grid[r][0] == 1 and not visited[r][0]:
                dfs(r, 0)
                
            # last column
            if grid[r][cols - 1] == 1 and not visited[r][cols - 1]:
                dfs(r, cols - 1)
        
        for c in range(cols):
            # first row
            if grid[0][c] == 1 and not visited[0][c]:
                dfs(0, c)
            
            # last row
            if grid[rows - 1][c] == 1 and not visited[rows - 1][c]:
                dfs(rows - 1, c)
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    count += 1
        return count