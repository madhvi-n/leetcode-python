class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        
        n = len(nums)
        ans = 0
        mid = n // 2
        # If length of array is even
        if n % 2 == 0:
            start = nums[mid]
            end = nums[mid - 1]
            ans = (start + end) / 2
            return ans
         
        # If length of array is odd
        else:
            return nums[mid]
