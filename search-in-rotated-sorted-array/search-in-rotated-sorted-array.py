class Solution:
    def binarySearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        while start <= end:
            mid = start + (end - start) // 2
            
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else: 
                return mid
        return -1
    
    def findPivot(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if mid < end and nums[mid] > nums[mid+1]:
                return mid
            
            if mid > start and nums[mid] < nums[mid-1]:
                return mid - 1
            
            if nums[mid] <= nums[start]:
                end = mid - 1
            else:
                start = mid + 1
                
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)

        if pivot == -1:
            return self.binarySearch(nums, target, 0, len(nums) - 1)
        
        if nums[pivot] == target:
            return pivot
        
        if target >= nums[0]:
            return self.binarySearch(nums, target, 0, pivot - 1)
        
        return self.binarySearch(nums, target, pivot + 1, len(nums) - 1)