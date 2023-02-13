class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ay2 - ay1) * (ax2 - ax1)
        area2 = (by2 - by1) * (bx2 - bx1)
        
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        x_overlap = right - left
        
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        y_overlap = top - bottom
        
        overlap_area = 0
        
        if x_overlap > 0 and y_overlap > 0:
            overlap_area = x_overlap * y_overlap
        
        total_area = area1 + area2 - overlap_area
        return total_area