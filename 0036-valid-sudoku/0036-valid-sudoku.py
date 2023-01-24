class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                
                if curr == ".":
                    continue
                    
                if curr in rows[i] or curr in cols[j] or curr in grid[i//3, j//3]:
                    return False
                
                rows[i].add(curr)
                cols[j].add(curr)
                grid[i//3, j//3].add(curr)
        
        return True