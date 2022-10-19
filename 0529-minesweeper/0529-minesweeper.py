class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        
        i, j = click[0], click[1]
        
        def dfs(row, col):
            if board[row][col] != "E":
                return
            
            mines = 0
            for x, y in [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]:
                dx, dy = row + x, col + y
                
                if 0 <= dx < rows and 0 <= dy < cols and board[dx][dy] == 'M':        
                    mines += 1
            
            if mines == 0:
                board[row][col] = 'B'
            else:
                board[row][col] = str(mines)
                return
            
            for x, y in [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]:
                dx, dy = row + x, col + y
                
                if 0 <= dx < rows and 0 <= dy < cols:
                    dfs(dx, dy)
            
        if not board:
            return []
        
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        dfs(i, j)
        return board
    