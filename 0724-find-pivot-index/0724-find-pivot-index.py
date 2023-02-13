class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
            
        leftSum = 0
        rightSum = total
        
        for i in range(len(nums)):
            rightSum -= nums[i]
            
            if leftSum == rightSum:
                return i
            
            leftSum += nums[i]
        return -1