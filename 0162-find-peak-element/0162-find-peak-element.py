class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == n - 1 or nums[mid] > nums[mid+1]):
                # mid is a peak element
                return mid
            
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                # peak must be in the left half of the array
                right = mid - 1
            else:
                # peak must be in the right half of the array
                left = mid + 1
        # no peak element found
        return -1