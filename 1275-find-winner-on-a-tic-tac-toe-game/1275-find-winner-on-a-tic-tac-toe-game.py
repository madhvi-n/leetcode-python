class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        colSums = [0 for x in range(3)]
        rowSums = [0 for x in range(3)]
        diag1Sum = 0
        diag2Sum = 0
        
        turn = 0
        for move in moves:
            if turn % 2 == 0:
                rowSums[move[0]] += 1
                colSums[move[1]] += 1
                if move[0] == move[1]:
                    diag1Sum += 1
                if move[0] == 2 - move[1]:
                    diag2Sum += 1
                
            else:
                rowSums[move[0]] -= 1
                colSums[move[1]] -= 1
                if move[0] == move[1]:
                    diag1Sum -= 1
                if move[0] == 2 - move[1]:
                    diag2Sum -= 1
                
            turn += 1
            
        if (3 in colSums) or (3 in rowSums) or \
            diag1Sum == 3 or diag2Sum == 3:
                return 'A'
            
        elif (-3 in colSums) or (-3 in rowSums) or \
            diag1Sum == -3 or diag2Sum == -3:
                return 'B'
        
        if len(moves) < 9:
            return 'Pending'
        else:
            return 'Draw'