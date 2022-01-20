class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        i = 0
        
        g.sort()
        s.sort()
        
        for ele in (s):
            if i < len(g) and ele >= g[i]:
                count +=1
                i +=1
        return count