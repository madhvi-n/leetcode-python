class Solution:
    def increasingMonotonic(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
    
    def decreasingMonotonic(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                return False
        return True

    def isMonotonic(self, nums: List[int]) -> bool:
        return self.increasingMonotonic(nums) or self.decreasingMonotonic(nums)