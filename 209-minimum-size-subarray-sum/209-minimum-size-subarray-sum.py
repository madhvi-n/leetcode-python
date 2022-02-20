class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        res = None
        
        for right in range(len(nums)):
            currSum += nums[right]
            
            while currSum >= target:
                res = min(res or float('inf'), right + 1 - left)
                currSum -= nums[left]
                left += 1
        return res or 0