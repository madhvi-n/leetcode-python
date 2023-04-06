class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n, ans = len(edges), 0
        scores = [0] * n
        for src, dest in enumerate(edges):
            scores[dest] += src
            
        for i, score in enumerate(scores):
            if score > scores[ans]:
                ans = i
        return ans
        
    