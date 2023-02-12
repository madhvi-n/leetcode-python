class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows, cols = [0] * m, [0] * n
        
        # count 1's for ith row and ith column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                    
        # traverse through matrix
        # if current cell is 1 and current row and col has frequency 1,
        # increment the count
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    count += 1
        return count