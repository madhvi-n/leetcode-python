class Solution:
    def dfs(self, src, adjMatrix, visited, component):
        pass
        
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        unionFind = dict()
        
        def find(x):
            unionFind.setdefault(x, x)
            if x != unionFind[x]:
                unionFind[x] = find(unionFind[x])
            return unionFind[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX > rootY:
                unionFind[rootX] = rootY
            else:
                unionFind[rootY] = rootX
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        res = []
        for c in baseStr:
            res.append(find(c))
        return ''.join(res)