class Solution:
    def minInsertions(self, s: str) -> int:
        # Base condition: Length of string is less than or equal to 1, return 0
        # If string in memo, return value from memo
        # Otherwise, compute as follows
        # - if first and last characters are equal, recursive call function for s[1:n-1]
        # - else recursively call function for s[1:n] and s[:n-1] and take min of the two plus 1 since we want min insertions
        # at the end store the result in memo for current string and return
        
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