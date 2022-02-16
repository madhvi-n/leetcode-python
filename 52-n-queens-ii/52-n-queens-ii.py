class Solution:
    def totalNQueens(self, n: int) -> int:
        column = set()
        positiveDiagonal = set() #r + i
        negativeDiagonal = set() #r - i
        
        result = []
        board = [["."] * n for i in range(n) ] 
        
        def backtrack(r: int):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c in column or (r + c) in positiveDiagonal or (r - c) in negativeDiagonal:
                    continue
                    
                column.add(c)
                positiveDiagonal.add(r + c)
                negativeDiagonal.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)
                
                column.remove(c)
                positiveDiagonal.remove(r + c)
                negativeDiagonal.remove(r - c)
                board[r][c] = "."
            
        backtrack(0)
        return len(result)