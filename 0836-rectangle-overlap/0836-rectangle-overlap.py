class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        A, B, C, D = rec1
        E, F, G, H = rec2
        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        if x1 < x2 and y1 < y2:
            return True
        return False