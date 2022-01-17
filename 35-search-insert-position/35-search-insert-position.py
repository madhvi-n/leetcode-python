class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        if target > nums[end]:
            return end + 1
        
        if target < nums[start]:
            return 0
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                end = mid - 1
            else: 
                start = mid + 1
                
        return start