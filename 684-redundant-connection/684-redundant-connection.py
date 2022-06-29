class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        length = len(edges)
        parent = [i for i in range(length + 1)]
        rank = [1 for i in range(length + 1)]
        
        
        def find(p):
            p = parent[p]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]
        
                