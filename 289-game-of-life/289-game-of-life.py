class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # Original | New | State
        #     0    |  0  |   0
        #     1    |  0  |   1
        #     0    |  1  |   2
        #     1    |  1  |   3
    
        rows, cols = len(board), len(board[0])
        
        
        def dfs(r, c):
            count = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i == r and j == c) or i == rows or j == cols or i < 0 or j < 0:
                        continue
                    if board[i][j] in [1, 3]:
                        count += 1
            return count
        
        
        for row in range(rows):
            for col in range(cols):
                neighbors = dfs(row, col)
                if board[row][col]:
                    if neighbors in [2, 3]:
                        board[row][col] = 3
                elif neighbors == 3:
                    board[row][col] = 2
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] in [2, 3]:
                    board[row][col] = 1
                    