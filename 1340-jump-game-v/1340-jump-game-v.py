class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = dict()
        
        def dfs(i, arr):
            if i in dp: 
                return dp[i]
            
            pathlen = 0
            
            for j in range(i + 1, i + d + 1):
                if len(arr) <= j or arr[j] >= arr[i]: 
                    break
                pathlen = max(dfs(j, arr), pathlen)
            
            for j in range(i-1, i-d-1,-1):
                if j < 0 or arr[j] >= arr [i]: 
                    break
                pathlen = max(dfs(j, arr), pathlen)  
            
            dp[i] = pathlen + 1
            return dp[i]

        longestpath = 0
        
        for i in range(len(arr)):
            longestpath = max(dfs(i, arr), longestpath)
        return longestpath