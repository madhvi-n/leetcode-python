class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correctIndex = nums[i]
            if nums[i] < len(nums) and nums[i] != nums[correctIndex]:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i += 1
            
        for i, num in enumerate(nums):
            if nums[i] != i:
                return i
        return len(nums)
            