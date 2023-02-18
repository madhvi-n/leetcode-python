class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        stoneSet = set(stones)
        visited = set()
        
        def jump(value, units):
            if (value + units not in stoneSet) or ((value, units) in visited) or units < 0:
                return False
            
            if value + units == stones[n - 1]:
                return True
            
            visited.add((value, units))
            
            return jump(value + units, units) or jump(value + units, units - 1) or jump(value + units, units + 1)
        return jump(stones[0], 1)