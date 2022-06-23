class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)
        indegree = dict.fromkeys(range(n), 0)
        count = 0
        queue = deque()
        stack = []
        
        for src, dest in edges:
            indegree[dest] += 1
            adjacency_list[src].append(dest)
        
        res = []
        
        for key, val in indegree.items():
            if val == 0:
                res.append(key)
        
        return res