class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        
        for i, num in enumerate(nums):
            max_sum = max(max_sum, num + curr_sum, num)
            curr_sum = max(num + curr_sum, num)
        return max_sum