class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        # count = 0
        # for i, j in enumerate(citations):
        #     if i < j:
        #         count += 1
        # return count
        return sum(i < j for i, j in enumerate(citations))