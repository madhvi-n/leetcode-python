class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        positive_sum = 0
        negative_sum = 0
        
        for num in nums:
            positive_sum = max(0, positive_sum + num)
            negative_sum = min(0, negative_sum + num)
            max_sum = max(max_sum, positive_sum,-negative_sum)
        return max_sum