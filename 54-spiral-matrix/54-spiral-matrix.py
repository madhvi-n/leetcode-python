class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowStart, rowEnd = 0, len(matrix)
        colStart, colEnd = 0, len(matrix[0])
        
        result = []
        
        while rowStart < rowEnd and colStart < colEnd:
            #Traversing through each element in top row
            for index in range(colStart, colEnd):
                result.append(matrix[rowStart][index])
            rowStart += 1
            
            
            #Traversing through each element in right column
            for index in range(rowStart, rowEnd):
                result.append(matrix[index][colEnd - 1])
            colEnd -= 1
            
            if not (rowStart < rowEnd and colStart < colEnd):
                break
                
            #Traversing through each element in bottom row
            for index in range(colEnd - 1, colStart - 1, -1):
                result.append(matrix[rowEnd - 1][index])
            rowEnd -= 1
                
            #Traversing through each element in middle row
            for index in range(rowEnd - 1, rowStart - 1, -1):
                result.append(matrix[index][colStart])
            colStart += 1
            
        return result
            