class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        sub_islands_count = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row == rows or col == cols or grid2[row][col] == 0:
                return True
            
            elif grid1[row][col] == 0 or grid2[row][col] == 0:
                return False
            
            elif grid1[row][col] == 1 and grid2[row][col] == 1:
                grid2[row][col] = 0
                top = dfs(row + 1, col)
                bottom = dfs(row - 1, col)
                right = dfs(row, col + 1)
                left = dfs(row, col - 1)
            return top and bottom and left and right
        
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and dfs(r, c):
                    sub_islands_count += 1
        return sub_islands_count