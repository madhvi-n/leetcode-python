class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        
        heap = []
        
        for num in nums:
            if len(heap) == 3:
                if heap[-1] < num:
                    heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
        
        if len(heap) == 1:
            return heap[0]
        
        elif len(heap) == 2:
            first_num = heap[0]
            heappop(heap)
            return max(first_num, heap[0])
        
        return heap[0]