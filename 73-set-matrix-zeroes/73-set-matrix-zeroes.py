class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        m, n = len(matrix), len(matrix[0])

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)

        for row in range(m):
            for col in range(n):
                if row in rows or col in cols:
                    matrix[row][col] = 0