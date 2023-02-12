class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
    
        rows, cols = len(matrix), len(matrix[0])
        res = []
        row_min, row_max, col_min, col_max = 0, rows - 1, 0, cols - 1

        while row_min <= row_max and col_min <= col_max:
            # Traverse top row
            for col in range(col_min, col_max + 1):
                res.append(matrix[row_min][col])

            # Traverse right column
            for row in range(row_min + 1, row_max + 1):
                res.append(matrix[row][col_max])

            if row_min < row_max and col_min < col_max:
                # Traverse bottom row
                for col in range(col_max - 1, col_min - 1, -1):
                    res.append(matrix[row_max][col])

                # Traverse left column
                for row in range(row_max - 1, row_min, -1):
                    res.append(matrix[row][col_min])

            # Adjust the boundaries and call the function recursively to traverse the inner matrix
            row_min += 1
            row_max -= 1
            col_min += 1
            col_max -= 1

        return res