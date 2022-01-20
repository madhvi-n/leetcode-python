class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        
        for i, num in enumerate(nums):
            if not num in count.keys():
                count[num] = 1
            else:
                count[num] += 1
            
        for key, val in count.items():
            if val == 1:
                return key