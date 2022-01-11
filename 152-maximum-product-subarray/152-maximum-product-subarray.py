class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMax, currentMin = 1, 1
        maxNum = nums[0]
        
        for num in nums:
            values = (num, num * currentMax, num * currentMin)
            currentMax, currentMin = max(values), min(values)
            maxNum = max(maxNum, currentMax)
        return maxNum
        