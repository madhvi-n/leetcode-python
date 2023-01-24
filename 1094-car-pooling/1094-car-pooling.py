class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        location = []
        
        for c, pickup, dropoff in trips:
            location += [(pickup, c)]
            location += [(dropoff,-c)]
        
        curr_capacity = 0
        
        for location, delta in sorted(location):
            curr_capacity += delta
            if curr_capacity > capacity:
                return False
        return True
            