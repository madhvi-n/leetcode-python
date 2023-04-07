class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = set()
        
        def dfs(source):
            for adjacent in range(N):
                if isConnected[source][adjacent] and adjacent not in visited:
                    visited.add(adjacent)
                    dfs(adjacent)
        
        ans = 0
        for i in range(N):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans