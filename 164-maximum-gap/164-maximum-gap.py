class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()
        
        max_diff = 0
        i, j = 0, 1
        
        while j < len(nums):
            max_diff = max(max_diff, nums[j] - nums[i])
            i += 1
            j += 1
        return max_diff
        