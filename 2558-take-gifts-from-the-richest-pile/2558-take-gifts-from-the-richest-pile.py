class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        res = []
        heap = []
        
        for gift in gifts:
            heapq.heappush(heap, -gift)
        
        while k:
            curr = math.isqrt(-heapq.heappop(heap))
            heappush(heap, -curr)
            k -= 1
        return -sum(heap)
