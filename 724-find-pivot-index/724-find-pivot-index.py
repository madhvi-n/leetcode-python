class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total, left_sum = sum(nums), 0
        
        for index, num in enumerate(nums):
            if total - num == 2 * left_sum:
                return index
            left_sum += num
        return -1
        
            