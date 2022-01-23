class Solution:    
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        length = len(nums)
        
        for i in range(32):
            cnt_ones = 0
            
            for j in range(length):
                cnt_ones += (nums[j] >> i) & 1
            
            total += cnt_ones * (length - cnt_ones)
        return total
            