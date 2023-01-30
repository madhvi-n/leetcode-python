class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        if n <= 1:
            return 0
        
        graph = defaultdict(list)
        
        for i in range(n):
            graph[arr[i]].append(i)
        
        
        queue = [0]
        visited = set([0])
        step = 0
        
        while queue:
            next_level = []
            
            # iterate the layer
            for node in queue:
                # check if node is reached
                if node == n - 1:
                    return step
                
                # check child nodes for curr node
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        next_level.append(child)
                        
                # clear the list to prevent redundant search
                graph[arr[node]].clear()
                
                # check neighbors of curr node
                for child in [node - 1, node + 1]:
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        next_level.append(child)
                
            queue = next_level
            step += 1
        
        return -1