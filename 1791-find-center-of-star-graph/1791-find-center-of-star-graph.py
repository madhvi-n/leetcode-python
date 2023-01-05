class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        center = 0
        for key, nodes in graph.items():
            if len(nodes) == len(edges):
                center = key
        return center
            