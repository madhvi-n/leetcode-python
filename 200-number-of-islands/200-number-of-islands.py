class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()
        
        def mark_current_island(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != "1":
                return
            
            visited.add((row, col))
            
            grid[row][col] = "2"
            mark_current_island(row + 1, col)
            mark_current_island(row - 1, col)
            mark_current_island(row, col + 1)
            mark_current_island(row, col - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    mark_current_island(r, c)
                    islands += 1
        return islands