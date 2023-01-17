class Solution:
    def isMonotonicIncreasing(self, arr):
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
    
    def isMonotonicDecreasing(self, arr):
        for i in range(0, len(arr) - 1):
            if arr[i] < arr[i + 1]:
                return False
        return True
    
    def isMonotonic(self, nums: List[int]) -> bool:
        return self.isMonotonicIncreasing(nums) or self.isMonotonicDecreasing(nums)
        