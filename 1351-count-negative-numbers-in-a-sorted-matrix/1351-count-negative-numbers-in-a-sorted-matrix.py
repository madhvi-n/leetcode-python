class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for nums in grid:
            for num in nums:
                if num < 0:
                    count += 1
                else:
                    continue
        return count