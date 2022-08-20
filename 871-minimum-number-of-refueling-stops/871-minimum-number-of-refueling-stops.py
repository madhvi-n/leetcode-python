class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        #Using Max heap
        
        stack = []
        stations.append((target, float('inf')))
        
        ans = prev = 0
        
        for location, capacity in stations:
            startFuel -= location - prev
            
            while stack and startFuel < 0:
                startFuel += -heapq.heappop(stack)
                ans += 1
            
            if startFuel < 0:
                return -1
            heapq.heappush(stack, -capacity)
            prev = location
        return ans