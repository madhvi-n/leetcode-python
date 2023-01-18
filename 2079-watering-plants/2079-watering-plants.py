class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        curr = capacity
        
        for i, x in enumerate(plants): 
            if curr < x: 
                steps += 2*i
                curr = capacity
            
            steps += 1
            curr -= x
        return steps