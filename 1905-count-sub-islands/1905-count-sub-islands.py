class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        subIslands = 0
        
        def mark_sub_islands(row, col):
            # if row, col is out of bounds or current cell in grid2 is 0, return True
            # if current cell is both grid is 0, return False
            # if current cell in both grid is 1, check for subislands recursively in 4 dirs
            # return top and bottom and left and right
            
            if row < 0 or col < 0 or row >= rows or col >= cols or grid2[row][col] == 0:
                return True
            
            elif grid1[row][col] == 0 and grid2[row][col] == 0:
                return False
             
            elif grid1[row][col] == 1 and grid2[row][col] == 1:
                grid2[row][col] = 0
                top = mark_sub_islands(row - 1, col)
                bottom = mark_sub_islands(row + 1, col)
                left = mark_sub_islands(row, col - 1)
                right = mark_sub_islands(row, col + 1)
                return top and bottom and left and right
            
        
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] and mark_sub_islands(r, c):
                    subIslands += 1
        return subIslands