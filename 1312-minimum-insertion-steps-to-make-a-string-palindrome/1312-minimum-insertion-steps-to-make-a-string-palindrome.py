class Solution:
    def minInsertions(self, s: str) -> int:
        def min_insertions(s, memo={}):
            if s in memo:
                return memo[s]

            n = len(s)
            if n <= 1:
                return 0

            if s[0] == s[n-1]:
                memo[s] = min_insertions(s[1:n-1], memo)
            else:
                memo[s] = 1 + min(min_insertions(s[1:n], memo), min_insertions(s[0:n-1], memo))

            return memo[s]
        return min_insertions(s)