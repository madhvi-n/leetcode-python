class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = 0
        for i, j in enumerate(citations[::-1]):
            if i < j:
                count += 1
        return count