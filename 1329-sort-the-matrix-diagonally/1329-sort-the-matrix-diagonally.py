class Solution:
    def diagonalSort(self, matrix: List[List[int]]) -> List[List[int]]:
        # Step 1: Create a dictionary to store the diagonals
        diagonals = {}

        # Step 2: Traverse the matrix row by row and add each element to the corresponding diagonal
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                key = i - j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(matrix[i][j])

        # Step 3: Sort each diagonal in the dictionary
        for key in diagonals:
            diagonals[key].sort()

        # Step 4: Traverse the matrix row by row again and replace each element with the next element in the corresponding diagonal
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                key = i - j
                matrix[i][j] = diagonals[key].pop(0)

        return matrix