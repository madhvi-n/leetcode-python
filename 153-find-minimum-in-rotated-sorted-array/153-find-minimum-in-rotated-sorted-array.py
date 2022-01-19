class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        res = min(nums[start], nums[end])
        
        while start <= end:
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break
                
            mid = start + (end - start) // 2
            res = min(nums[mid], res)
            
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return res