class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
#         n = len(nums)
        
#         answer = 0
        
#         for left in range(n):
#             min_val, max_val = float('inf'), float('-inf')
#             for right in range(left, n):
#                 max_val = max(max_val, nums[right])
#                 min_val = min(min_val, nums[right])
#                 answer += max_val - min_val
#         return answer

        n, answer = len(nums), 0 
        stack = []
        
        # Find the sum of all the minimum.
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        # Find the sum of all the maximum.
        stack.clear()
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)
        
        return answer