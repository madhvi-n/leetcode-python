class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        # return no of lands cells
        def dfs(row, col):
            if row < 0 or col < 0 or row == ROWS or col == COLS or (row, col) in visited or not grid[row][col]:
                return 0
            visited.add((row, col))
            res = 1 # we are at land cell and now look in 4 directions for possible land
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for dx, dy in directions:
                res += dfs(row + dx, col + dy)
            return res

        land, borderLand = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c]
                # checking grid is 1 and not visited and lies on the edge of the grid/perimeter
                if grid[r][c] and (r, c) not in visited and (c in [0, COLS - 1] or r in [0, ROWS - 1]):
                    borderLand += dfs(r, c)

        return land - borderLand