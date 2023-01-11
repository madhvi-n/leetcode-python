class Solution:
    def dfs(self, i, j):
        if i < 0 or j < 0 or i >=self.rows or j >= self.cols or self.board[i][j] != "O":
            return
        self.board[i][j] = 'T'
        neighbors = [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]
        for x, y in neighbors:
            self.dfs(x, y)
    
    def solve(self, board):
        if not board: 
            return 0
        
        self.board, self.rows, self.cols = board, len(board), len(board[0])
        
        for i in range(0, self.rows):
            self.dfs(i, 0)
            self.dfs(i, self.cols - 1)
            
        for j in range(0, self.cols):
            self.dfs(0, j)
            self.dfs(self.rows - 1, j)
        
        for i,j in product(range(self.rows), range(self.cols)):
            board[i][j] = "X" if board[i][j] != "T" else "O"
        