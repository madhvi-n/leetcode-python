class Solution:
    def numTrees(self, n: int) -> int:    
        memo = {}
        memo[0] = 1
        memo[1] = 1
        memo[2] = 2
        
        def helper(n):
            if n in memo:
                return memo[n]
            total = 0
            for i in range(n):
                current = helper(i) * helper(n - 1 - i)
                total += current
            memo[n] = total
            return memo[n]
        return helper(n)