class Solution:
    def minMoves(self, nums: List[int]) -> int:
        total, minNum = 0, float('inf')
        
        for num in nums:
            total += num
            minNum = min(minNum, num)
        return total - len(nums) * minNum
