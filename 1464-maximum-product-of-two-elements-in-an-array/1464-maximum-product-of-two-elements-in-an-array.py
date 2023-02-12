class Solution:
    def maxProduct(self, nums: List[int]) -> int:
#         n = len(nums)
#         maxcurr = float('-inf')
        
#         for i in range(n):
#             for j in range(i + 1, n):
#                 curr = (nums[i] - 1) * (nums[j] - 1)
#                 maxcurr = max(maxcurr, curr)
        
#         return maxcurr

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            
            if len(heap) > 2:
                heapq.heappop(heap)
        
        a, b = heap
        return (a - 1) * (b - 1)