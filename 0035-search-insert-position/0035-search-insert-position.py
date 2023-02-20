class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search from 0 to end index
        # Find mid
        # if mid == target: return mid index
        # if nums[mid] < target: left = mid + 1 i.e search RHS
        # if nums[mid] > target: right = mid - 1 i.e search LHS
        # return left pointer
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left