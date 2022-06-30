class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        visited = set()
        adjacency = defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    adjacency[i+1].append(j+1)
                    adjacency[j+1].append(i+1)
        
        def dfs(source):
            for adjacent in adjacency[source]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    dfs(adjacent)
        ans = 0
        
        for i in range(1, n+1):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans