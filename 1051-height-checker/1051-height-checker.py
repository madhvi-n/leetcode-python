class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights)
        
        for i, height in enumerate(heights):
            if heights[i] != expected[i]:
                count += 1
        return count