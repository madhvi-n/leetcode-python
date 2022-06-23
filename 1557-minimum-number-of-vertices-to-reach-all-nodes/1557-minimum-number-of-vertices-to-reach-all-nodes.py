class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)
        indegree = [0] * n
        
        for src, dest in edges:
            indegree[dest] += 1
            adjacency_list[src].append(dest)
        
        res = []
        
        for index, val in enumerate(indegree):
            if val == 0:
                res.append(index)
        return res