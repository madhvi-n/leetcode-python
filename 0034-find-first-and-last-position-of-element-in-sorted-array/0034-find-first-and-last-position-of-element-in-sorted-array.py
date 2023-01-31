class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchFirstLast(left, right, isFirst):
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target or (isFirst and nums[mid] == target):
                    right = mid
                else:
                    left = mid + 1
            return left
        
        if not nums:
            return [-1, -1]
        
        first = searchFirstLast(0, len(nums), True)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        
        last = searchFirstLast(first, len(nums), False) - 1
        return [first, last]