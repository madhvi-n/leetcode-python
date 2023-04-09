class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums is None:
            return False
        
        low, high = 0, len(nums) - 1
        
        while low <= high:
            while low < high and nums[low] == nums[low + 1]:
                low += 1
            while low < high and nums[high] == nums[high - 1]:
                high -= 1
            
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return True
            
            if nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target <= nums[high] and target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False