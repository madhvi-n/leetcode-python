import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since python has min heap, turning them negative
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second) #since first is greater than second element   

        # if stones are none, 0 will be returned else element at index 0 will be returned
        stones.append(0)
        return abs(stones[0])

        