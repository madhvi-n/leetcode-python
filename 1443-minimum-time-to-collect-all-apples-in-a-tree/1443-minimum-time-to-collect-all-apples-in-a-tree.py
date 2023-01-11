class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjacencyList = defaultdict(list)
        
        for src, dest in edges:
            adjacencyList[src].append(dest)
            adjacencyList[dest].append(src)
        
        visited = set()
        
        def dfs(node, parent):
            total = 0
            
            if node in visited:
                return total
                
            visited.add(node)

            for child in adjacencyList[node]:
                if child != parent:
                    childTime = dfs(child, node)

                    if childTime > 0 or hasApple[child]:
                        total += childTime + 2
            return total
        
        return dfs(0, -1)