class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        closed_islands = 0
        seen = set()

        def is_closed_islands(row, col):
            if row < 0 or row == rows or col < 0 or col == cols:
                return False

            if grid[row][col] == 1:
                return True

            grid[row][col] = 1
            seen.add((row, col))
            top = is_closed_islands(row - 1, col)
            bottom = is_closed_islands(row + 1, col)
            left = is_closed_islands(row, col - 1)
            right = is_closed_islands(row, col + 1)
            return top and bottom and left and right

        for row in range(1, rows - 1):
            for column in range(1, cols - 1):
                if grid[row][column] == 0 and (row, column) not in seen:
                    if is_closed_islands(row, column):
                        closed_islands += 1
        return closed_islands