class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        adjacencyList = defaultdict(list)
        self.longestPath = 1
        
        for i in range(1, n):
            adjacencyList[parent[i]].append(i)
        
        def dfs(node):
            if node not in adjacencyList:
                return 1
            
            currentPath = 1
            for child in adjacencyList[node]:
                childPath = dfs(child)
                if s[node] != s[child]:
                    self.longestPath = max(self.longestPath, childPath + currentPath)
                    currentPath = max(currentPath, childPath + 1)
            return currentPath
        
        dfs(0)
        return self.longestPath