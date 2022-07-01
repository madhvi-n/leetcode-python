class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        visited = set()
        
        def dfs(i):
            for j in range(n) :
                if matrix[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans