class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        curr_far = curr_end = 0
        
        for i in range(n - 1):
            if i + nums[i] > curr_far:
                curr_far = i + nums[i]
             
            if i == curr_end:
                ans += 1
                curr_end = curr_far
        
        return ans