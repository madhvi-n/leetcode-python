import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        # since python has min heap, turning them negative
        for stone in stones:
            heapq.heappush(heap, -1 * (stone))

        while len(heap) > 1:
            first = -1 * heapq.heappop(heap)
            second = -1 * heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -1 * (first - second)) #since first is greater than second element   

        return abs(heap[0]) if heap else 0

        