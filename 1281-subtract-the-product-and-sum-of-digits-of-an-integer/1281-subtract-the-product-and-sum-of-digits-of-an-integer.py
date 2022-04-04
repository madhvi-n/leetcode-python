class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(str(n))
        
        product = int(nums[0])
        total = int(nums[0])
        
        for i in range(1, len(nums)):
            product *= int(nums[i])
            total += int(nums[i])
        
        return product - total