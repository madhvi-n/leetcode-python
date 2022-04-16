from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, n, result = deque([0]), len(nums), []

        for i in range(n):
            while queue and queue[0] <= i - k:
                queue.popleft()
            
            while queue and nums[i] >= nums[queue[-1]] :
                queue.pop()
            
            queue.append(i)
            
            result.append(nums[queue[0]])
            
        return result[k-1:]