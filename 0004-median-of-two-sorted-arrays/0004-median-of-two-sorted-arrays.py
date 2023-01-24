class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        
        n = len(nums)
        
        if n % 2 != 0:
            return nums[n//2]
        
        else:
            mid = n // 2
            a, b = nums[mid], nums[mid - 1]
            print(a, b)
            return (a + b) / 2
        
            