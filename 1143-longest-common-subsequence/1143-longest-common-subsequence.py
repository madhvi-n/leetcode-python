class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str, index1 = 0, index2 = 0):
        memo = dict()

        def recurse(index1 = 0, index2 = 0):
            key = (index1, index2)

            if key in memo:
                return memo[key]
            elif index1 == len(t1) or index2 == len(t2):
                memo[key] = 0
            elif t1[index1] == t2[index2]:
                memo[key] = 1 + recurse(index1 + 1, index2 + 1)
            else:
                memo[key] = max(recurse(index1 + 1, index2), recurse(index1, index2 + 1))
            return memo[key]
        return recurse(0, 0)