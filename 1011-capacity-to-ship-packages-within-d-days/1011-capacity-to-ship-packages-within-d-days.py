class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = max(weights), sum(weights)
        
        while start < end:
            mid = start + (end - start) // 2
            
            total, subarrays = 0, 1
            
            for i, num in enumerate(weights):
                if total + num > mid:
                    total = num
                    subarrays += 1
                else:
                    total += num
                    
            
            if subarrays > days:
                start = mid + 1
            else: 
                end = mid
        return end