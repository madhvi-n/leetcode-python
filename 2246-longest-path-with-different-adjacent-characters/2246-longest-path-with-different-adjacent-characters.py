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
            
            longest, secondLongest = 0, 0
            
            for child in adjacencyList[node]:
                longestFromChild = dfs(child)
                
                if s[node] == s[child]:
                    continue
                
                if longestFromChild > longest:
                    secondLongest, longest = longest, longestFromChild
                    
                elif longestFromChild > secondLongest:
                    secondLongest = longestFromChild
                    
            self.longestPath = max(self.longestPath, longest + secondLongest + 1)
            return longest + 1
        
        dfs(0)
        return self.longestPath