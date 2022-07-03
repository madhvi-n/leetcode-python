class Solution:
    def totalNQueens(self, n: int) -> int:
        column = set()
        positiveDiagonal = set() #r + c
        negativeDiagonal = set() #r - c
        board = [["."] * n for i in range(n) ] 
        count = 0
        
        def backtrack(r: int):
            nonlocal count
            if r == n:
                count += 1
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
        return count