class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
#         res = 0
#         # a xor a = 0
#         
#         for num in nums:
#             res ^= num
#         return res

        left, right, mid = 0, len(nums) - 1, 0
        while left <= right:
            
            mid = (left + right) >> 1
            
            isHalfEven = (mid - left) % 2 == 0
            
            if mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                if isHalfEven: 
                    left = mid + 2
                else: 
                    right = mid - 1
            elif mid and nums[mid] == nums[mid-1]:
                if isHalfEven: 
                    right = mid - 2
                else: 
                    left = mid + 1
            else: 
                return nums[mid]
