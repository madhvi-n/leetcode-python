class DSU:
    def __init__(self, n):
				# Initially each element is its own parent
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x] # return root of the set

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        # if x and y belongs to different set
        # if rank of Y is greater than X, set Y as parent of X
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            
        # If rank of X is greater than Y, set X as the parent of Y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            
        # Else Set Y as the parent of X and increment Y's rank or vice versa
        # The idea is if both are same, pick any combination
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1
                
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # find dislikes which belong to different groups
        # use union find
        # create an adj list using dislikes
        # init a dsu for n + 1
        # for each node, for child of each node, if parent of node and child are same, return False
        adj = defaultdict(list)
        
        for x, y in dislikes:
            adj[x].append(y)
            adj[y].append(x)
        
        dsu = DSU(n + 1)
        
        for node in range(1, n + 1):
            for child in adj[node]:
                if dsu.find(node) == dsu.find(child):
                    return False
                dsu.union(adj[node][0], child)
        return True
            
        
        