class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # Initialize sum over two diagonals as 0
        primarySum, secondarySum = 0, 0
        
        rowStart, colEnd = 0, len(mat[0]) - 1
        
        while rowStart < len(mat) and colEnd >= 0:
            primarySum += mat[rowStart][rowStart]
            
            if rowStart != colEnd:
                secondarySum += mat[rowStart][colEnd]
            
            rowStart += 1
            colEnd -= 1
        
        return primarySum + secondarySum
            
        
        
        