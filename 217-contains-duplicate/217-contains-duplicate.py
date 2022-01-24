class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        
        for i, num in enumerate(nums):
            if not num in count.keys():
                count[num] = 1
            else:
                count[num] += 1
            
        for key, val in count.items():
            if val >= 2:
                return True
        
        return False