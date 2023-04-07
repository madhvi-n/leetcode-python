class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # We can use a recursive function dfs to explore all possible paths from a given cell. For each neighbor of the current cell with a greater value, we can continue the search, updating the length of the current path accordingly. We can keep track of the maximum path length seen so far and return it as the final result.
        
#         if not matrix:
#             return 0

#         m, n = len(matrix), len(matrix[0])
#         max_path = 0

#         def dfs(i, j, path_length):
#             nonlocal max_path

#             max_path = max(max_path, path_length)

#             for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
#                 if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
#                     dfs(x, y, path_length+1)

#         for i in range(m):
#             for j in range(n):
#                 dfs(i, j, 1)

#         return max_path


        """
        We can initialize the DP table with all zeros.

        Then, we can explore the matrix in a topological order. For each cell (i, j), 
        we can explore its four neighbors (up, down, left, right), and if the neighbor has a 
        greater value than the current cell, we can update its DP value by adding 1 to the DP value of the current cell.
        Finally, we can iterate over the DP table and return the maximum value.
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_length = 1

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(x, y))
            dp[i][j] += 1
            return dp[i][j]

        for i in range(m):
            for j in range(n):
                max_length = max(max_length, dfs(i, j))

        return max_length