class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if coins == 0 or not costs:
            return 0
        
        costs.sort()
        count = 0
        
        for cost in costs:
            if cost <= coins:
                coins -= cost
                count += 1
                
            if coins == 0:
                break
        
        return count
        
        