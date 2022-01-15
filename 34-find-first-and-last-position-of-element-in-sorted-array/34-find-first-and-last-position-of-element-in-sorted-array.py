class Solution:
    def binarySearch(self, nums: List[int], target: int, findStartIndex: bool) -> int:
        ans, start, end = -1, 0, len(nums) -1
        
        while start <= end:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                ans = mid
                if findStartIndex:
                    end = mid - 1
                else: 
                    start = mid + 1
        return ans
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        ans[0] = self.binarySearch(nums, target, True)
        if ans[0] != -1:
            ans[1] = self.binarySearch(nums, target, False)
        return ans
        