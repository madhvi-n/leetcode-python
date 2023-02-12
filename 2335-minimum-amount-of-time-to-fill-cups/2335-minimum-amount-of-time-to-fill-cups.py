class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap = []
        for a in amount:
            heapq.heappush(heap, -a)
            
        seconds = 0
        while heap[0] != 0:
            max1 = heappop(heap)
            max2 = heappop(heap)
            seconds += 1
            heappush(heap, max1 + 1)
            heappush(heap, max2 + 1)
        return seconds