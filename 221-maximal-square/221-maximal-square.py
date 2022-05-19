class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:        
        rows = len(matrix)
        cols = len(matrix[0])
        max_edge = 0
        
        for row in range(rows):
            for col in range(cols):
                #calculate max edge if row == 0 or col == 0
                if row == 0 or col == 0:
                    max_edge = max(max_edge, int(matrix[row][col]))
                
                # if current cell is 1, current cell = min of (top cell, left cell and diagonal left cell) + 1 
                elif matrix[row][col] == '1':
                    matrix[row][col] = str(min(max_edge, int(matrix[row-1][col-1]),
                        int(matrix[row-1][col]), int(matrix[row][col-1])) + 1)
                    
                    max_edge = max(max_edge, int(matrix[row][col]))
        for grid in matrix:
            print(grid)
        return max_edge ** 2                    