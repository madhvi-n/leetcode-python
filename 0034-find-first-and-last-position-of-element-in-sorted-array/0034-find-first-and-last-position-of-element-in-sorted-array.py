class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(left, right, isFirst):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target or (isFirst and nums[mid] == target):
                    right = mid - 1 
                else:
                    left = mid + 1
            return left
        
        
        if not nums:
            return [-1, -1]
        
        n = len(nums)
        first = helper(0, n - 1, True)
        
        if first == n or nums[first] != target:
            return [-1, -1]
        
        last = helper(first, n - 1, False) - 1
        
        return [first, last]