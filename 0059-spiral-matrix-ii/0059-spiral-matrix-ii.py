class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        row_min, row_max, col_min, col_max = 0, n - 1, 0, n - 1
        num = 1

        while row_min <= row_max and col_min <= col_max:
            # Fill top row
            for col in range(col_min, col_max + 1):
                res[row_min][col] = num
                num += 1

            # Fill right column
            for row in range(row_min + 1, row_max + 1):
                res[row][col_max] = num
                num += 1

            if row_min < row_max and col_min < col_max:
                # Fill bottom row
                for col in range(col_max - 1, col_min - 1, -1):
                    res[row_max][col] = num
                    num += 1

                # Fill left column
                for row in range(row_max - 1, row_min, -1):
                    res[row][col_min] = num
                    num += 1

            # Adjust the boundaries
            row_min += 1
            row_max -= 1
            col_min += 1
            col_max -= 1

        return res