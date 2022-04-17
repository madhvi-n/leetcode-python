import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grid = collections.defaultdict(set)
        
        
        for r in range(len(board)):
            for c in range(len(board)):
                #Ignore empty cells
                if board[r][c] == ".":
                    continue
                
                #If element exist in any of the three sets, return False
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grid[r//3, c//3]:
                    return False
                
                #Add element if it doesn't exist
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grid[(r//3, c//3)].add(board[r][c])
                
        return True
        