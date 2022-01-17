class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end = max(nums), sum(nums)
        
        while start < end:
            mid = start + (end - start) // 2
            
            total, subarrays = 0, 1
            
            for i, num in enumerate(nums):
                if total + num > mid:
                    total = num
                    subarrays += 1
                else:
                    total += num
                    
            
            if subarrays > m:
                start = mid + 1
            else: 
                end = mid
        return end        
        