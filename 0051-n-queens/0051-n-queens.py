class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        positiveDiagonal = set()  # (r + c)
        negativeDiagonal = set()  # (r - c)

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in columns or (r + c) in positiveDiagonal or (r - c) in negativeDiagonal:
                    continue

                columns.add(c)
                positiveDiagonal.add(r + c)
                negativeDiagonal.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                columns.remove(c)
                positiveDiagonal.remove(r + c)
                negativeDiagonal.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res