class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[None for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[len(s)][len(p)] = 1
        
        for i in range(len(p)-1, -1, -1):
            dp[len(s)][i] = dp[len(s)][i+1] if p[i] == '*' else 0
        
        for j in range(len(s)):
            dp[j][len(p)] = 0
        
        self.dfs_helper(s, p, 0, 0, dp)
        return dp[0][0] == 1
    
    def dfs_helper(self, s, p, sp, pp, dp):
        if dp[sp][pp] is not None:
            return dp[sp][pp]
        
        if sp < len(s) and (s[sp] == p[pp] or p[pp] == '?'):
            dp[sp][pp] = self.dfs_helper(s, p, sp+1, pp+1, dp)
        
        elif pp < len(p) and p[pp] == '*':
            resultOne = self.dfs_helper(s, p, sp+1, pp, dp) # matching seq with *
            resultTwo = self.dfs_helper(s, p, sp, pp+1, dp) # matching * with empty string
            resultThree = self.dfs_helper(s, p, sp+1, pp+1, dp) # end matching seq with * and inc both
            dp[sp][pp] = 1 if (resultOne + resultTwo + resultThree) > 0 else 0
            
        else:
            dp[sp][pp] = 0
            
        return dp[sp][pp]
                